import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_importance

import pickle

class Model():
    def __init__(self):
        self.loaded_model = pickle.load(open("static/upt_model.pickle.dat", "rb"))

    def make_data(self,df_data):
        # 첫번째 컬럼빼고 다음에 나오는 부위컬럼들 삭제
        drop_idx = []
        for i in range(0, len(df_data)-4, 4):
            drop_idx.append(i+3)
        
        df_data.drop(df_data.index[drop_idx], inplace = True)
        df_data.reset_index(drop=True, inplace = True)
        
        # 모든 값 str -> float형태로 
        df_data = df_data.apply(pd.to_numeric)
        
        # posenet score 모을 리스트 생성
        score_idx = []
        for i in range(0, len(df_data), 3):
            score_idx.append(i+2)
            
        # score점수가 0.5이하면 버리기 -> NaN값으로 처리
        columns = df_data.columns.to_list()
        for idx in score_idx:  
            for column in columns:    
                if df_data.loc[idx][column] < 0.5:
                    df_data.loc[idx-2][column] = np.nan # x  'NaN'
                    df_data.loc[idx-1][column] = np.nan # y
                    
        # x, y 좌표만 남기기
        df_data = df_data.drop(df_data.index[score_idx])
        df_data.reset_index(drop=True, inplace = True)
        
        # x좌표 index, y좌표 index 용 리스트 생성
        x_idx = []
        y_idx = []
        for idx in range(0, len(df_data), 2):
            x_idx.append(idx)
            y_idx.append(idx+1)
            
        # x_data, y_data분리
        x_data = df_data.loc[x_idx, :]
        x_data.reset_index(drop=True, inplace = True)

        y_data = df_data.loc[y_idx, :]
        y_data.reset_index(drop=True, inplace = True)
        
        # 컬럼명 바꾸기용 리스트 생성
        x_col = []
        y_col = []
        for column in columns:
            x_col.append(column+'_x')
            y_col.append(column+'_y')
            
        # 컬럼명 바꾸기 
        x_data.columns = x_col
        y_data.columns = y_col
        
        # 모두 합치기
        all_data = pd.concat([x_data, y_data], axis = 1)
        all_data = all_data.apply(pd.to_numeric)
        
        return all_data #이 결과를

    def predict(self, data):
        result = self.make_data(data)
        y_pred = self.loaded_model.predict(result)
        predictions = [round(value) for value in y_pred]
        return predictions