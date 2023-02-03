import pandas as pd
import random
import copy

All_timetable = []
while 1:
    n = input("학급 수를 입력:")
    # n = 학급 수
    N = int(input("과목 개수를 입력:"))
    # N = 과목 개수
    subject = []
    # 과목 리스트
    subject_times = []
    # 과목별 총 시간
    subject_min = []
    # 과목별 하루 최소 시간
    i = 0
    Total_times = 0
    # 총 합 시간
    while i < N:
        # 40시간 분류 하기 위한 while 문 ( 플라스크로 실행할 땐 필요 없음)
        a = input("과목을 적으시오:")
        subject.append(a)
        b = int(input("과목의 횟수를 적으시오:"))
        subject_times.append(b)
        Total_times += b
        i += 1

    if Total_times > 40:
        # 40시간 구별 if문
        print("입력시간이 40시간을 넘었습니다")
        continue
    else:
        break

# 데이터프레임에 요일 넣기(5의 배수)
if Total_times % 5 == 0:
    ind_num = Total_times // 5
    col = ["월", "화", "수", "목", "금"]
    ind = []
    for i in range(1, ind_num + 1):
        ind.append(i)
    con = []

# 일단 5의 배수일 때 아래 코드를 실행
# (몫의 나머지만큼 데이터프레임을 추가로 넣을 필요 없는 코드)

# respectively_day_subject_array = 각 요일별 과목이 들어갈 2차원 배열형태의 리스트
# 아래 코드를 통해 [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None] ...(5개) 만들어짐]
row, column = 5, 5
respectively_day_subject_array = [[None for j in range(column)] for i in range(row)]
# 과목을 뿌리기 전 None의 상태

for i in range(int(n)):  # 학급 수 만큼 테이블 생성
    df = pd.DataFrame(con, columns=col, index=ind)
    All_timetable.append(df)

for i in range(5):
    for j in range(5):
        df[i][j] = respectively_day_subject_array[i][j]

for i in range(col):
    for j in range(row):

        if (type(df[j][i]) == type(df[j][i])):  # 이 경우 모든 타입이 스트링이거나,
            if (type(df[j][i] == 'str')):  # 모든 타입이 None(빈칸)이거나의 경우
                print("과목을 넣지 않고 다시 뽑는 함수 실행")
            else:
                print("과목을 집어넣는 함수 실행")
        elif (type(df[j][i]) != type(df[j][i])):  # 빈칸이 1개 정도는 남아 있는 경우(else로 바꾸기 가능)
            print("과목을 집어넣는 함수 실행")


# 중간 변수 이름 정리
# n : 학급 수
# N : 과목 개수
# subject = [] : 과목을 저장하는 리스트
# subject_times = [] : 과목별 총 시간을 저장하는 리스트
# subject_min = [] : 과목별 하루 최소 시간을 저장하는 리스트


# 횟수 많은 과목을 구하는 용도의 리스트 만들기 함수(리스트 정렬)
def Creating_sorted_Lists(subject, subject_times):
    # 인덱스가 일치하게 내림차순으로 정렬된 두 리스트
    sorted_subject = []
    sorted_subject_times = []

    for i in range(len(subject_times)):
        Max = max(subject_times)
        Max_order = subject_times.index(Max)
        sorted_subject.append(subject[Max_order])
        sorted_subject_times.append(Max)
        del subject_times[Max_order]
        del subject[Max_order]


def

    # 여기서부터 수정해야 할 부분
    for i in range(int(n)):  # 학급 수 만큼 테이블 생성
        df = pd.DataFrame(con, columns=col, index=ind)
        All_timetable.append(df)
        subject_copy = copy.deepcopy(subject)
        subject_times_copy = copy.deepcopy(subject_times)
        for j in range(5):  # 중복을 빼기 위해 월~금을 중심으로 시작
            class_subject = []
            random_subjects = random.sample(subject_copy, ind_num)
            class_subject.extend(random_subjects)
            if i > 0:
                m = 0
                while m < i:
                    l = 0
                    while l < ind_num:
                        if All_timetable[m].iloc[l, j] == class_subject[l]:
                            class_subject = []
                            random_subjects = random.sample(subject_copy, ind_num)
                            class_subject.extend(random_subjects)
                            l = 0
                            continue
                        else:
                            l += 1
                    m += 1

            for l in range(len(random_subjects)):
                random_subject = random_subjects[l]
                subject_order = subject_copy.index(random_subject)
                subject_times_copy[subject_order] -= 1
                if subject_times_copy[subject_order] == 0:
                    del subject_copy[subject_order]
                    del subject_times_copy[subject_order]
            df[df.columns[j]] = class_subject


for x in All_timetable:
    print(x)
