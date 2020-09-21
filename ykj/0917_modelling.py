#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_importance

path = "./all_posnet_data/"


# In[2]:


data1 = pd.read_csv(path+"all_data_1.csv")
data2 = pd.read_csv(path+"all_data_2.csv")
data3 = pd.read_csv(path+"all_data_3.csv")
data4 = pd.read_csv(path+"all_data_4.csv")

label = pd.read_excel(path+"all_data_label.xlsx", header = None, index_col = 1)


# In[3]:


# 첫번째 컬럼빼고 다음에 나오는 컬럼들 삭제
drop_idx1 = []
for i in range(0, len(data1)-4, 4):
    drop_idx1.append(i+3)
    
drop_idx2 = []
for i in range(0, len(data2)-4, 4):
    drop_idx2.append(i+3)
    
drop_idx3 = []
for i in range(0, len(data3)-4, 4):
    drop_idx3.append(i+3)
    
drop_idx4 = []
for i in range(0, len(data4)-4, 4):
    drop_idx4.append(i+3)

data1.drop(data1.index[drop_idx1], inplace = True)
data1.reset_index(drop=True, inplace = True)

data2.drop(data2.index[drop_idx2], inplace = True)
data2.reset_index(drop=True, inplace = True)

data3.drop(data3.index[drop_idx3], inplace = True)
data3.reset_index(drop=True, inplace = True)

data4.drop(data4.index[drop_idx4], inplace = True)
data4.reset_index(drop=True, inplace = True)


# In[4]:


# 4개 csv 파일 합치기
frames = [data1, data2, data3, data4]
data = pd.concat(frames, axis = 0)


# In[5]:


# 합친 데이터 인덱스 재설정 및 데이터 타입 변환
data.reset_index(drop=True, inplace = True)
data = data.apply(pd.to_numeric)


# In[6]:


# posenet score 모을 리스트 생성
score_idx = []
for i in range(0, len(data), 3):
    score_idx.append(i+2)


# In[7]:


# score점수가 0.5이하면 버리기 -> NaN값으로 처리
columns = data.columns.to_list()
for idx in score_idx:  
    for column in columns:    
        if data.loc[idx][column] < 0.5:
            data.loc[idx-2][column] = np.nan # x  'NaN'
            data.loc[idx-1][column] = np.nan # y


# In[8]:


# score data만 떼어내기 -> 2346row
score_data = data.loc[score_idx , :]
score_data.reset_index(drop=True, inplace = True)


# In[9]:


# x, y 좌표만 남기기
data = data.drop(data.index[score_idx])
data.reset_index(drop=True, inplace = True)


# In[10]:


# x좌표 index, y좌표 index 용 리스트 생성
x_idx = []
y_idx = []
for idx in range(0, len(data), 2):
    x_idx.append(idx)
    y_idx.append(idx+1)


# In[11]:


# x_data, y_data분리
x_data = data.loc[x_idx, :]
x_data.reset_index(drop=True, inplace = True)

y_data = data.loc[y_idx, :]
y_data.reset_index(drop=True, inplace = True)


# In[12]:


# 컬럼명 바꾸기용 리스트 생성
x_col = []
y_col = []
for column in columns:
    x_col.append(column+'_x')
    y_col.append(column+'_y')


# In[13]:


# 컬럼명 바꾸기 
x_data.columns = x_col
y_data.columns = y_col


# In[14]:


# 라벨링한 csv파일 전처리 
value = {'classification':label[2]}
label = pd.DataFrame(value, index = label.index)
label.reset_index(drop=True, inplace = True)


# In[15]:


# 모두 합치기
all_data = pd.concat([x_data, y_data, label], axis = 1)


# In[16]:


# 각 행의 모든 컬럼에서 null값이 20개 이상인 행 제거 => 1419rows
data_20 = all_data.drop(all_data.index[all_data.isnull().sum(axis = 1)>19])
data_20.reset_index(drop=True, inplace = True)


# In[17]:


# Decision Tree와 data_20.info(), XGBoost 특성중요도에서 얻은 특성값
feature_names =['leftShoulder_y','leftEye_y','rightElbow_x','rightShoulder_y',
                'leftShoulder_x','leftElbow_x','rightEye_x','leftElbow_y',
                'rightShoulder_x','rightWrist_x','leftWrist_x'] #11개


# In[67]:


# 모든 특성 학습시키기 
X = data_20[feature_names]
y = data_20[data_20.columns[-1]]

#데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 66)

#모델 학습
model = XGBClassifier(
        learning_rate =0.09,
        n_estimators=110,
        max_depth=7,
        min_child_weight=1,
        gamma=0.3,
        reg_alpha=1e-05,
        subsample=0.61,
        colsample_bytree=0.7,
        seed = 150
) 
model.fit(X_train, y_train)

#평가 
print("훈련 세트 정확도: {:.3f}".format(model.score(X_train, y_train)))
print("테스트 세트 정확도 : {:.3f}".format(model.score(X_test, y_test)))


# In[68]:


# # 예측
# X_data = []
# X_new = pd.DataFrame(X_data, columns = columns) 
# # 들어오는 값이 어떻게 될지 몰라 우선 x,y축 다른 행에 있다 가정하고 columns 지정.
# # 들어온 값 형태에 따라 추후 수정필요
# pre = model.predict(X_new)
# print(pre)


# In[ ]:




