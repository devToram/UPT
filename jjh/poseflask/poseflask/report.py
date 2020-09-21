import numpy as np
import pandas as pd
from numpy.linalg import norm

class Report():
    def __init__(self):
        self.data = [0,0,0,1,0,0,1,0,0,0]
        self.key= ["nose","leftEye","rightEye","leftEar","rightEar","leftShoulder","rightShoulder","leftElbow","rightElbow","leftWrist","rightWrist","leftHip","rightHip","leftKnee","rightKnee","leftAnkle","rightAnkle"]
        self.feedback_part ={
            "시선" : "시선에 따라서 자세가 바뀌게 될 뿐 아니라 고개를 들어서 시선을 앞이나 위에 둬서 고개를 너무 숙이게 되면 목에 부담을 줄 수 있습니다. 몸과 머리가 일직선이 될 수 있게 시선은 바닥을 향해주세요.",
            "귀" : "(머리) 머리에서 발까지 일직선을 만드는 게 플랭크 자세의 올바른 운동법입니다. 머리가 앞으로 빠져서 날개뼈가 튀어나오지 않게 해주세요. ",
            "어깨" : "어깨와 지면이 수직을 이루도록 해주세요. 어깨가 밑으로 가라 앉게되면 어깨에 무리를 줄 수 있습니다. 또한 승모근의 발달이 생길 수 있으니 유의 바랍니다.",
            "팔꿈치" : "어깨 아래 팔꿈치가 수직으로 올 수 있도록 위치해주세요.",
            "손목" : "손목과 팔 어깨가 일직선이 되게 펴서 수직이 되게 해주세요. 잘못된 각도는 손목에 무리가 갈 수 있습니다.",
            "엉덩이" : "엉덩이 뜨지 않게 끌어내리고 허리가 아래 쪽으로 처지지 않도록 긴장시켜주세요.",
            "무릎" : "머리 끝부터 발끝까지 긴장감을 만들기 위해 무릎이 구부러지지 않게 주의해주세요. ",
            "발목" : "발목 모아주세요. 잘못된 발목 위치는 허리와 엉덩이가 일직선 되는 밸런스를 무너뜨리는 원인이 됩니다."
        }

    def made(self,result_list):
        result_list_2 = []
        for i in result_list:
            a_xy = i[:34]
            score_list = i[34:]
            x_list = []
            y_list = []
            
            
            for j in range(len(a_xy)):
                if j == 0:
                    x_list.append(a_xy[j])
                elif j % 2 == 0 :
                    x_list.append(a_xy[j])
                else:
                    y_list.append(a_xy[j])
            result_list_2.append([x_list,y_list,score_list])
            
        return result_list_2

    def made_dataframe(self,input_):
        key= ["nose","leftEye","rightEye","leftEar","rightEar","leftShoulder","rightShoulder","leftElbow","rightElbow","leftWrist","rightWrist","leftHip","rightHip","leftKnee","rightKnee","leftAnkle","rightAnkle"]
        input_data = pd.DataFrame(columns = key)
        idx = 0
        for i in range(len(input_)):
            x_ = input_[i][0]
            y_ = input_[i][1]
            score_ = input_[i][2]
            
            for j in range(4):
                if j == 0:
                    input_data.loc[j + idx] =x_
                elif j == 1:
                    input_data.loc[j + idx] =y_
                elif j == 2:
                    input_data.loc[j + idx] =score_
                else:
                    input_data.loc[j + idx] =key
            idx += 4
        return input_data


#======================================================================================================================================
#======================================================================================================================================
# model_result_b = [0,0,0,1,0,0,1,0,0,0]                             # 10개데이터 들어왔을때 예시 
#======================================================================================================================================
#======================================================================================================================================
#model_result_a = [1,0,1,0,0,1,0,1,1,0]                                                                # 10개데이터 들어왔을때
#======================================================================================================================================
#======================================================================================================================================
#model_result_c = [1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0]                       #데이터 31개 test

#model_result_d =[0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0]

#model_result_e =[0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0]


# key= ["nose","leftEye","rightEye","leftEar","rightEar","leftShoulder","rightShoulder","leftElbow","rightElbow","leftWrist","rightWrist","leftHip","rightHip","leftKnee","rightKnee","leftAnkle","rightAnkle"]
# feedback_part ={
#     "시선" : "시선에 따라서 자세가 바뀌게 될 뿐 아니라 고개를 들어서 시선을 앞이나 위에 둬서 고개를 너무 숙이게 되면 목에 부담을 줄 수 있습니다. 몸과 머리가 일직선이 될 수 있게 시선은 바닥을 향해주세요.",
#     "귀" : "(머리) 머리에서 발까지 일직선을 만드는 게 플랭크 자세의 올바른 운동법입니다. 머리가 앞으로 빠져서 날개뼈가 튀어나오지 않게 해주세요. ",
#     "어깨" : "어깨와 지면이 수직을 이루도록 해주세요. 어깨가 밑으로 가라 앉게되면 어깨에 무리를 줄 수 있습니다. 또한 승모근의 발달이 생길 수 있으니 유의 바랍니다.",
#     "팔꿈치" : "어깨 아래 팔꿈치가 수직으로 올 수 있도록 위치해주세요.",
#     "손목" : "손목과 팔 어깨가 일직선이 되게 펴서 수직이 되게 해주세요. 잘못된 각도는 손목에 무리가 갈 수 있습니다.",
#     "엉덩이" : "엉덩이 뜨지 않게 끌어내리고 허리가 아래 쪽으로 처지지 않도록 긴장시켜주세요.",
#     "무릎" : "머리 끝부터 발끝까지 긴장감을 만들기 위해 무릎이 구부러지지 않게 주의해주세요. ",
#     "발목" : "발목 모아주세요. 잘못된 발목 위치는 허리와 엉덩이가 일직선 되는 밸런스를 무너뜨리는 원인이 됩니다."
# }

    def out_put_x_score(self,input_data_b, model_result_b):                                           #return score_x, avr_1, avr_0
        count = 3
        drop_count = len(model_result_b) - 1
        for i in range(drop_count):                                                                            
            input_data_b = input_data_b.drop(input_data_b.index[count])                                       # 중간 껴있는 컬럼 삭제
            count = count + 3

            #==============================================================================================================================================
            #==============================================================================================================================================
            #==============================================================================================================================================

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
        for i in self.key:
            sum_ = 0
            for j in input_data_b_x_0_[i]:
                sum_ =  sum_ + float(j)
            sum_list_0.append(sum_)
                                                                                                                # 컬럼별 합 -> 리스트
        sum_list_1 = []
        for i in self.key:
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
        score_x = 100 - int(euclidean_distance(document_1,document_2))
        print("나의 동작 평균 점수 :",score_x,"점", " ( 좌 우 )") 

        return score_x, avr_1, avr_0
        #===========================================================
    def out_put_y_score(self,input_data_b, model_result_b):                                           #return score_y, avr_1_y, avr_0_y

        count = 3
        drop_count = len(model_result_b) - 1
        for i in range(drop_count):                                                                            
            input_data_b = input_data_b.drop(input_data_b.index[count])                                       # 중간 껴있는 컬럼 삭제
            count = count + 3

        result_idx_1_ = []
        result_idx_0_ = []
        for i in range(len(model_result_b)):
                                                                                                            # 1값과 0값 분류
            if model_result_b[i] == 1:
                result_idx_1_.append(i)
            else:
                result_idx_0_.append(i)

        result_idx_1_y = []
        for i in result_idx_1_:
            result_idx_1_y.append(i*4 + 1)

        result_idx_0_y = []
        for i in result_idx_0_:
            result_idx_0_y.append(i*4 + 1)

        input_data_a_y_1 = input_data_b.loc[result_idx_1_y]
        input_data_a_y_0 = input_data_b.loc[result_idx_0_y]


        sum_list_0_y = []
        for i in self.key:
            sum_ = 0
            for j in input_data_a_y_0[i]:
                sum_ =  sum_ + float(j)
            sum_list_0_y.append(sum_)


        sum_list_1_y = []
        for i in self.key:
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
        score_y = 100 - int(euclidean_distance(document_1_y,document_2_y))
        print("나의 동작 평균 점수 :",score_y,"점", " ( 상 하 )")
        
        return score_y, avr_1_y, avr_0_y

    def feedback(self,part, feedback_part):
            r_list = []
            for i in feedback_part:
                for j in part:
                    if i == j:
                        r_list.append(feedback_part[i])
            return r_list
    #==========================================================================================================
    def report_x(self,s):
        score = s[0]
        avr_1 = s[1]
        avr_0 = s[2]
        
        def comment_x(c,avr_1,avr_0):

            document_1 = np.array(avr_1)
            document_2 = np.array(avr_0)
            sub = document_1-document_2
                                                                                                                    # 1평균 - 0평균 
                                                                                                                    


            sub_dict = dict()
            for i in range(len(sub)):
                                                                                                                    #1평균 - 0평균  딕셔너리 만들기
                for j in self.key[i:]:
                    sub_dict[j] = sub[i]
                    break

            abs_sub = abs(sub)

                                                                                                                    #절대값 
            result_dict = dict()

            for i in range(len(abs_sub)):
                                                                                                                    #절대값 딕셔너리
                for j in self.key[i:]:
                    result_dict[j] = abs_sub[i]
                    break
        
            result_dict_sorted = sorted(result_dict, key = lambda x: result_dict[x], reverse = True)
                                                                                                                        #절대값 value 크기로 내림정렬 
            comment_position = []
            comment_position_1 =[]                                                                                                            #  
            for i in result_dict_sorted[:c]:
                                                                                                                        #1평균 - 0평균 양수 음수 
                                                                                                                        # 절대값 딕셔너리
                                                                                                                    # 위에서 4개값의 sub값 음수 양수로 앞뒤 코멘트
                if sub_dict[i] > 0:
                    # print(i,float('%10.4f'%(result_dict[i]+0.00005)),'앞으로 땡기세요')
                    # comment_position_1.append(i+str(float('%10.4f'%(result_dict[i]+0.00005)))+'뒤로 빼세요')
                    # +str(float('%10.4f'%(result_dict[i]+0.00005)))
                    if i == 'leftEye' or i == 'rightEye' :
                        comment_position.append("시선")
                        comment_position_1.append("시선" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftEar" or i == "rightEar" :
                        comment_position.append("귀")
                        comment_position_1.append("귀" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == 'leftShoulder' or i == 'rightShoulder' :
                        # print("어깨에 위치에 주의해주세요.")
                        comment_position.append("어깨")
                        comment_position_1.append("어깨" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftElbow" or i == "rightElbow" :
                        comment_position.append("팔꿈치")
                        comment_position_1.append("팔꿈치" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftWrist" or i == "rightWrist" :
                        comment_position.append("손목")
                        comment_position_1.append("손목" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftHip" or i == "rightHip":
                        comment_position.append("엉덩이")
                        comment_position_1.append("엉덩이" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftKnee" or i == "rightKnee":
                        comment_position.append("무릎")
                        comment_position_1.append("무릎" + "("+ i + ")  "+'뒤로 빼세요')
                    elif i == "leftAnkle":
                        comment_position.append("발목")
                        comment_position_1.append("발목" + "("+ i + ")  "+'뒤로 빼세요')
                    
            

                else:                                                                                                        #소수점 5에서 반올림
                    # print(i,float('%10.4f'%(result_dict[i]+0.00005)), "뒤로 빼세요.")
                    # comment_position_1.append(i+str(float('%10.4f'%(result_dict[i]+0.00005)))+'앞으로 당기세요')
                    
                    if i == 'leftEye' or i == 'rightEye':
                        comment_position.append("시선")
                        comment_position_1.append("시선" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftEar" or i == "rightEar":
                        comment_position.append("귀")
                        comment_position_1.append("귀" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == 'leftShoulder' or i == 'rightShoulder':
                        comment_position.append("어깨")
                        comment_position_1.append("어깨" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftElbow" or i == "rightElbow":
                        comment_position.append("팔꿈치")
                        comment_position_1.append("팔꿈치" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftWrist" or i == "rightWrist":
                        comment_position.append("손목")
                        comment_position_1.append("손목" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftHip" or i == "rightHip":
                        comment_position.append("엉덩이")
                        comment_position_1.append("엉덩이" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftKnee" or i == "rightKnee":
                        comment_position.append("무릎")
                        comment_position_1.append("무릎" + "("+ i + ")  "+'앞으로 당기세요')
                    elif i == "leftAnkle":
                        comment_position.append("발목")
                        comment_position_1.append("발목" + "("+ i + ")  "+'앞으로 당기세요')
                    
            # print(comment_position_1)
            return comment_position , comment_position_1



        



        if score > 85:
            print("전체적인 좌우 중심 밸런스가 좋습니다!\n지금처럼 정확한 동작을 유지하면서 꾸준히 운동해주세요 ")
            print()
            return None
        elif 70 < score <= 85:
            print("전체적인 좌우 중심 밸런스가 다소 안좋습니다!")
            print(comment_x(1,avr_1,avr_0)[0],'위치에 주의해주세요.')
            # print(comment_x(1,avr_1,avr_0)[1])
            [print(i) for i in comment_x(1,avr_1,avr_0)[1] ]
            # print(feedback(comment_x(1,avr_1,avr_0)[0],feedback_part))
            [print(i) for i in self.feedback(comment_x(1,avr_1,avr_0)[0],self.feedback_part) ]
            

            print()
            return None
        elif 55 < score <= 70:
            print("전체적인 좌우 중심 밸런스가 안좋습니다!")
            print(comment_x(2,avr_1,avr_0)[0],'위치에 주의해주세요')
            # print(comment_x(2,avr_1,avr_0)[1])
            [print(i) for i in comment_x(2,avr_1,avr_0)[1]]
            # print(feedback(comment_x(2,avr_1,avr_0)[0],feedback_part))
            [print(i) for i in self.feedback(comment_x(2,avr_1,avr_0)[0],self.feedback_part)]
            print()
            return None
        elif 40 < score <= 55:
            print("전체적인 좌우 중심 밸런스가 매우 안좋습니다!")
            print(comment_x(3,avr_1,avr_0)[0],'위치에 주의해주세요')
            # print(comment_x(3,avr_1,avr_0)[1])
            [print(i) for i in comment_x(3,avr_1,avr_0)[1]]
            print(self.feedback(comment_x(3,avr_1,avr_0)[0],self.feedback_part))
            
            
            print()
        elif score<50:
            print("다시 배우슈")
            return None

        # #================Y========================
        #                                                                                                        #    x와 거의 동일    위 아래 코멘트
    def report_y(self,s):
        score = s[0]
        avr_1_y = s[1]
        avr_0_y = s[2]

        def comment_y(c,avr_1_y, avr_0_y):

            document_1_y = np.array(avr_1_y)
            document_2_y = np.array(avr_0_y)

            sub_y = document_1_y-document_2_y

            sub_dict_y = dict()
            for i in range(len(sub_y)):
        
                for j in self.key[i:]:
                    sub_dict_y[j] = sub_y[i]
                    break

            abs_sub_y = abs(sub_y)


            result_dict_y = dict()

            for i in range(len(abs_sub_y)):
                for j in self.key[i:]:
                    result_dict_y[j] = abs_sub_y[i]
                    break
            
            result_dict_y_sorted = sorted(result_dict_y, key = lambda x: result_dict_y[x], reverse = True)

            comment_position = []
            comment_position_1 =[]
            
            for i in result_dict_y_sorted[:c]:

                if sub_dict_y[i] > 0:
                    # print(i,float('%10.4f'%(result_dict_y[i]+0.00005)),'올리세요')
                    # comment_position_1.append(i + str(float('%10.4f'%(result_dict_y[i]+0.00005))) + "올리세요")
                    # +str(float('%10.4f'%(result_dict_y[i]+0.00005)))
                    if i == 'leftEye' or i == 'rightEye':
                        comment_position.append("시선")
                        comment_position_1.append("시선" + "("+ i + ")  "+'올리세요')
                    elif i == "leftEar" or i == "rightEar":
                        comment_position.append("귀")
                        comment_position_1.append("귀" + "("+ i + ")  "+'올리세요')
                    elif i == 'leftShoulder' or i == 'rightShoulder':
                        
                        comment_position.append("어깨")
                        comment_position_1.append("어깨" + "("+ i + ")  "+'올리세요')
                    elif i == "leftElbow" or i == "rightElbow":
                        comment_position.append("팔꿈치")
                        comment_position_1.append("팔꿈치" + "("+ i + ")  "+'올리세요')
                    elif i == "leftWrist" or i == "rightWrist":
                        comment_position.append("손목")
                        comment_position_1.append("손목" + "("+ i + ")  "+'올리세요')
                    elif i == "leftHip" or i == "rightHip":
                        comment_position.append("엉덩이")
                        comment_position_1.append("엉덩이" + "("+ i + ")  "+'올리세요')
                    elif i == "leftKnee" or i == "rightKnee":
                        comment_position.append("무릎")
                        comment_position_1.append("무릎" + "("+ i + ")  "+'올리세요')
                    elif i == "leftAnkle":
                        comment_position.append("발목")
                        comment_position_1.append("발목" + "("+ i + ")  "+'올리세요')
                    
                else:
                    # print(i,float('%10.4f'%(result_dict_y[i]+0.00005)), "내리세요.")
                    # comment_position_1.append(i + str(float('%10.4f'%(result_dict_y[i]+0.00005))) + "내리세요")
                    
                    if i == 'leftEye' or i == 'rightEye':
                        comment_position.append("시선")
                        comment_position_1.append("시선" + "("+ i + ")  "+"내리세요")
                    elif i == "leftEar" or i == "rightEar":
                        comment_position.append("귀")
                        comment_position_1.append("귀" + "("+ i + ")  "+"내리세요")
                    elif i == 'leftShoulder' or i == 'rightShoulder':
                        # print("어깨에 위치에 주의해주세요.")
                        comment_position.append("어깨")
                        comment_position_1.append("어깨" + "("+ i + ")  "+"내리세요")
                    elif i == "leftElbow" or i == "rightElbow":
                        comment_position.append("팔꿈치")
                        comment_position_1.append("팔꿈치" + "("+ i + ")  "+"내리세요")
                    elif i == "leftWrist" or i == "rightWrist":
                        comment_position.append("손목")
                        comment_position_1.append("손목" + "("+ i + ")  "+"내리세요")
                    elif i == "leftHip" or i == "rightHip":
                        comment_position.append("엉덩이")
                        comment_position_1.append("엉덩이" + "("+ i + ")  "+"내리세요")
                    elif i == "leftKnee" or i == "rightKnee":
                        comment_position.append("무릎")
                        comment_position_1.append("무릎" + "("+ i + ")  "+"내리세요")
                    elif i == "leftAnkle":
                        comment_position.append("발목")
                        comment_position_1.append("발목" + "("+ i + ")  "+"내리세요")
                    
            # print(comment_position_1)
            return comment_position , comment_position_1




        if score > 85:
            print("전체적인 상하 중심 밸런스가 좋습니다!\n지금처럼 정확한 동작을 유지하면서 꾸준히 운동해주세요! ")
            print()
            return None
        elif 70 < score <= 85:
            print("전체적인 상하 중심 밸런스가 다소 안좋습니다!")
            print(comment_y(1,avr_1_y, avr_0_y)[0],"위치에 주의 해주세요.")
            # print(comment_y(1,avr_1_y, avr_0_y)[1])
            [print(i) for i in comment_y(1,avr_1_y, avr_0_y)[1]]
            print(self.feedback(comment_y(1,avr_1_y,avr_0_y)[0],self.feedback_part))
            print()
            return None
        elif 55 < score <= 70:
            print("전체적인 상하 중심 밸런스가  안좋습니다!")
            print(comment_y(2,avr_1_y, avr_0_y)[0],"위치에 주의 해주세요.")
            # print(comment_y(2,avr_1_y, avr_0_y)[1])
            [print(i) for i in comment_y(2,avr_1_y, avr_0_y)[1]]
            print(self.feedback(comment_y(2,avr_1_y,avr_0_y)[0],self.feedback_part))
            print()
            return None
        elif 40 < score <= 55:
            print("전체적인 상하 중심 밸런스가 매우 안좋습니다!")
            print(comment_y(3,avr_1_y, avr_0_y)[0],"위치에 주의 해주세요.")
            # print(comment_y(3,avr_1_y, avr_0_y)[1])
            [print(i) for i in comment_y(3,avr_1_y, avr_0_y)[1]]
            print(self.feedback(comment_y(3,avr_1_y,avr_0_y)[0],self.feedback_part))
            print()
        elif score<50:
            print("다시 배우슈")
            return None
    






# print('--------------------------------------------------------------------------')
# report_x(out_put_x_score(input_data_a,model_result_a))
# report_y(out_put_y_score(input_data_a,model_result_a))
# print('--------------------------------------------------------------------------')
# print()
# report_x(out_put_x_score(input_data_b,model_result_b))
# report_y(out_put_y_score(input_data_b,model_result_b))
# print('--------------------------------------------------------------------------')
# print()
# report_x(out_put_x_score(input_data_c,model_result_c))
# report_y(out_put_y_score(input_data_c,model_result_c))

# print('--------------------------------------------------------------------------')
# print()
# report_x(out_put_x_score(input_data_d,model_result_d))
# report_y(out_put_y_score(input_data_d,model_result_d))

# print('--------------------------------------------------------------------------')
# print()
# report_x(out_put_x_score(input_data_e,model_result_e))
# report_y(out_put_y_score(input_data_e,model_result_e))


# print('--------------------------------------------------------------------------')
# print()