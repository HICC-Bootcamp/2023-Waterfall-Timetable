import pandas as pd
import random
while 1:
    n=input("학급 수를 입력:") # n = 학급 수
    N=int(input("과목 개수를 입력:")) #N = 과목 개수
    subject=[] #과목 리스트
    subject_times=[] # 과목별 총 시간
    subject_min=[] # 과목별 하루 최소 시간
    i=0 
    Total_times=0 # 총 합 시간
    while i < N: # 40시간 분류 하기 위한 while문(플라스크로 실행할땐 필요 없음)
        a=input("과목을 적으시오:")
        subject.append(a)
        b=int(input("과목의 횟수를 적으시오:"))
        subject_times.append(b)
        Total_times+=b
        i+=1
        
    if Total_times>40: #40시간 구별 if문
        print("입력시간이 40시간을 넘었습니다")
        continue
    else:
        break
subject_result=list(zip(subject,subject_times))
print(subject_result) #과목과 과목 횟수를 묶는 함수


# 과목별 하루 최소 시간 계산
def div(a):
    a=a//5
    subject_min.append(a)


list(map(div,subject_times))

if Total_times % 5 == 0 :
    ind_num = Total_times//5
else:
    ind_num = Total_times//5 + 1
All_timetable = []
col = ["월", "화","수","목","금"]
ind = []
for i in range(1,ind_num+1):
    ind.append(i)
con = []
ft = pd.DataFrame(con, columns=col, index=ind)
All_timetable.append(ft)
st = pd.DataFrame(con, columns=col, index=ind)
All_timetable.append(st)
for x in All_timetable:
    print(x)
