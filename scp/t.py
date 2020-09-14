import numpy as np
import pandas as pd
from numpy.linalg import norm

#======================================================================================================================================
#======================================================================================================================================
model_result_b = [0,0,0,1,0,0,1,0,0,0]
input_data_b = pd.read_csv(r'./test_data_10_b.csv',encoding="EUC-KR")                                 # 10개데이터 들어왔을때 예시 
#======================================================================================================================================
#======================================================================================================================================
model_result_a = [1,0,1,0,0,1,0,1,1,0]                                                                # 10개데이터 들어왔을때
input_data_a = pd.read_csv(r'./test_data_10_a.csv',encoding="EUC-KR")
#======================================================================================================================================
#======================================================================================================================================
model_result_c = [1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0]                       #데이터 31개 test
input_data_c = pd.read_csv(r'./test_data_31.csv',encoding="EUC-KR")


# print(input_data_b)
                                                        


def out_put(input_data_b, model_result_b):
    count = 3
    drop_count = len(model_result_b) - 1
    for i in range(drop_count):                                                                            
        input_data_b = input_data_b.drop(input_data_b.index[count])                                       # 중간 껴있는 컬럼 삭제
        count = count + 3

        #==============================================================================================================================================
        #==============================================================================================================================================
        #==============================================================================================================================================
    key= ["nose","leftEye","rightEye","leftEar","rightEar","leftShoulder","rightShoulder","leftElbow","rightElbow","leftWrist","rightWrist","leftHip","rightHip","leftKnee","rightKnee","leftAnkle","rightAnkle"]

            
    result_idx_1_ = []
    result_idx_0_ = []
    for i in range(len(model_result_b)):
                                                                                                         # 1값과 0값 분류
        if model_result_b[i] == 1:
            result_idx_1_.append(i)
        else:
            result_idx_0_.append(i)
                                                                                      
    result_idx_1_x_ = []
    for i in result_idx_1_:
        result_idx_1_x_.append(i*4)
                                                                                                         # 1데이터 인덱스


    result_idx_0_x_ = []
    for i in result_idx_0_:                                                                            # 0데이터 인덱스
        result_idx_0_x_.append(i*4)
    

    input_data_b_x_1_ = input_data_b.loc[result_idx_1_x_]                                                #1,0 데이터
    input_data_b_x_0_ = input_data_b.loc[result_idx_0_x_]

    sum_list_0 = []
    for i in key:
        sum_ = 0
        for j in input_data_b_x_0_[i]:
            sum_ =  sum_ + float(j)
        sum_list_0.append(sum_)
                                                                                                            # 컬럼별 합 -> 리스트
    sum_list_1 = []
    for i in key:
        sum_ = 0
        for j in input_data_b_x_1_[i]:
            sum_ =  sum_ + float(j)
        sum_list_1.append(sum_)

    avr_1 = [] 
    for i in sum_list_1:
        avr_1.append(i/len(result_idx_1_x_))
                                                                                                             #컬럼별 합 평균 구하기
    avr_0 = [] 
    for i in sum_list_0:
        avr_0.append(i/len(result_idx_0_x_))


    def euclidean_distance(A, B):
        return np.linalg.norm(A-B)
                                                                                                              #유클리드 거리 
    document_1 = np.array(avr_1)
    document_2 = np.array(avr_0)
    print("앞 뒤 유사도 :",euclidean_distance(document_1,document_2),"0에 가까울수록 좋음") 
    #===========================================================

    document_1 = np.array(avr_1)
    document_2 = np.array(avr_0)
    sub = document_1-document_2
                                                                                                                  # 1평균 - 0평균 
                                                                                                                  


    sub_dict = dict()
    for i in range(len(sub)):
                                                                                                                   #1평균 - 0평균  딕셔너리 만들기
        for j in key[i:]:
            sub_dict[j] = sub[i]
            break

    abs_sub = abs(sub)

                                                                                                                   #절대값 
    result_dict = dict()

    for i in range(len(abs_sub)):
                                                                                                                   #절대값 딕셔너리
        for j in key[i:]:
            result_dict[j] = abs_sub[i]
            break
    
    result_dict_sorted = sorted(result_dict, key = lambda x: result_dict[x], reverse = True)
                                                                                                                    #절대값 value 크기로 내림정렬 
                                                                                                                    #  
    for i in result_dict_sorted[:4]:
                                                                                                                    #1평균 - 0평균 양수 음수 
                                                                                                                    # 절대값 딕셔너리
                                                                                                                    # 위에서 4개값의 sub값 음수 양수로 앞뒤 코멘트
        if sub_dict[i] > 0:
            print(i,float('%10.4f'%(result_dict[i]+0.00005)),'앞으로 땡기세요')
        else:                                                                                                        #소수점 5에서 반올림
            print(i,float('%10.4f'%(result_dict[i]+0.00005)), "뒤로 빼세요.")


    #================Y========================
                                                                                                           #    x와 거의 동일    위 아래 코멘트

    result_idx_1_y = []
    for i in result_idx_1_:
        result_idx_1_y.append(i*4 + 1)

    result_idx_0_y = []
    for i in result_idx_0_:
        result_idx_0_y.append(i*4 + 1)

    input_data_a_y_1 = input_data_b.loc[result_idx_1_y]
    input_data_a_y_0 = input_data_b.loc[result_idx_0_y]


    sum_list_0_y = []
    for i in key:
        sum_ = 0
        for j in input_data_a_y_0[i]:
            sum_ =  sum_ + float(j)
        sum_list_0_y.append(sum_)


    sum_list_1_y = []
    for i in key:
        sum_ = 0
        for j in input_data_a_y_1[i]:
            sum_ =  sum_ + float(j)
        sum_list_1_y.append(sum_)


    avr_1_y = [] 
    for i in sum_list_1_y:
        avr_1_y.append(i/len(result_idx_1_y))

    avr_0_y = [] 
    for i in sum_list_0_y:
        avr_0_y.append(i/len(result_idx_0_y))

    def euclidean_distance(A, B):
        return np.linalg.norm(A-B)

    document_1_y = np.array(avr_1_y)
    document_2_y = np.array(avr_0_y)
    print("위 아래 유사도 :",euclidean_distance(document_1_y,document_2_y),"  (0에 가까울수록 좋은자세)")            
    #================================================================

    document_1_y = np.array(avr_1_y)
    document_2_y = np.array(avr_0_y)

    sub_y = document_1_y-document_2_y

    sub_dict_y = dict()
    for i in range(len(sub)):
    
        for j in key[i:]:
            sub_dict_y[j] = sub_y[i]
            break

    abs_sub_y = abs(sub_y)


    result_dict_y = dict()

    for i in range(len(abs_sub_y)):
        for j in key[i:]:
            result_dict_y[j] = abs_sub_y[i]
            break
        
    result_dict_y_sorted = sorted(result_dict_y, key = lambda x: result_dict_y[x], reverse = True)


    for i in result_dict_y_sorted[:4]:

        if sub_dict_y[i] > 0:
            print(i,float('%10.4f'%(result_dict_y[i]+0.00005)),'올리세요')
        else:
            print(i,float('%10.4f'%(result_dict_y[i]+0.00005)), "내리세요.")


print("##########################################################################")
out_put(input_data_b, model_result_b)

print("##########################################################################")
print("##########################################################################")
out_put(input_data_a, model_result_a)

print("##########################################################################")
print("##########################################################################")
out_put(input_data_c, model_result_c)

#==================================================================================================================================