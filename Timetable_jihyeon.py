import pandas as pd
import random
import copy

# Timetable__how_to_create_the_timetables
# 1.   표 만들기
# 2.   월~금 Type 비교
# - (1) 같을시 >> 모두 빈칸인지 비교
# - (2) 다를시 >> 빈칸이 1개는 무조건 있음
# 3.   횟수 많은 과목부터 나열
# 4.   과목별 횟수만큼 요일 수 선택
# 5.   요일 중 빈자리 선택
# 6.   자리가 빈칸인지 아닌지 확인
# 7.   전 반이랑 비교해서 5번으로 돌아가기

# 선택한 자리에 넣고 비교하고 >> 겹치면 삭제
# 선택만 하고 비교해서 안겹치면 추가


# Timetable_kind_of_functions
# 1. main() : 실질적 실행 함수
# 2. dis_five(Total_times) : 5의 배수를 판별하는 함수
# 3. make_Df(All_timetable, n, col, ind, con) : 리스트에 DataFrame을 추가하는 함수(=3차원 배열을 만드는 함수)
# 4. com_full_with_string(con, ind_num, remains_day_index) : 요일(colnums)의 리스트가 str으로 모두 채워졌는지의 여부를 검사하는 함수
# 5. creating_sorted_Lists(subject, subject_times) : 시수가 많은 과목을 구하는 용도의 리스트 만들기 함수(리스트 정렬 함수)
# 6. selecting_day_as_the_number_of_subjects(remains_day_index, sorted_subject, sorted_subject_times) : 과목별 횟수 만큼 요일 수를 선택하는 함수
# 7. selecting_empty_space_from_days(remains_day_index, selected_days) : 요일 중 빈자리에 과목(str)을 넣는 함수
# 8. comparing_with_maken_timetable_before() : 전에 만들어졌던 시간표와 중복되는 시간표가 만들어지는 경우를 방지하는 함수


def main():
    # 전역변수 선언
    # n : 학급 수
    # N : 과목 개수
    # subject = [] : 과목을 저장하는 리스트
    # subject_times = [] : 과목별 총 시간을 저장하는 리스트
    # subject_min = [] : 과목별 하루 최소 시간을 저장하는 리스트
    # Total_times : 총 합 시간

    All_timetable = []
    n = input("학급 수를 입력:")
    N = int(input("과목 개수를 입력:"))
    subject = []
    subject_times = []
    subject_min = []
    Total_times = 0
    i = 0

    # 시간표 생성에 필요한 기본값 받기
    while i < N:
        a = input("과목을 적으시오:")
        subject.append(a)
        b = int(input("과목의 횟수를 적으시오:"))
        subject_times.append(b)
        Total_times += b
        i += 1

    ind_num, col, ind, con = dis_five(Total_times)
    All_timetable, remains_day_index = make_Df(All_timetable, n, col, ind, con)
    remains_day_index = com_full_with_string(con, ind_num, remains_day_index)
    sorted_subject, sorted_subject_times = creating_sorted_Lists(subject, subject_times)
    selected_days = selecting_day_as_the_number_of_subjects(remains_day_index, sorted_subject, sorted_subject_times)


    selecting_empty_space_from_days(remains_day_index, selected_days)
    comparing_with_maken_timetable_before)()






# 5의 배수 판별하는 함수
def dis_five(Total_times):
    if Total_times % 5 == 0:
        # ind_num : 행의 개수(변수)
        ind_num = Total_times // 5
        # col = [] : 요일 리스트
        col = ["월", "화", "수", "목", "금"]
        # ind = [] : 세로줄 리스트
        ind = []
        for i in range(1, ind_num + 1):
            ind.append(i)
        # 내용
        con = []
    return ind_num, col, ind, con


# 리스트에 DataFrame을 추가하는 함수(=3차원 배열을 만드는 함수)
def make_Df(All_timetable, n, col, ind, con):
    # 남은 요일 인덱스
    remains_day_index = [0, 1, 2, 3, 4]
    for i in range(int(n)):
        df = pd.DataFrame(con, columns=col, index=ind)
        All_timetable.append(df)
    return All_timetable, remains_day_index


#
# for i in range(5):
#     for j in range(5):
#         df[i][j] = respectively_day_subject_array[i][j]

# 이 경우 모든 타입이 스트링이거나, # 모든 타입이 None(빈칸)이거나의 경우

#
#     for i in range(col):
#         while True:
#             for j in range(row):
#                 if(type(df[0][i]) == type(df[j][i])):
#                     if (type(df[0][i] == 'str')):
#                         print("과목을 넣지 않고 다시 뽑는 함수 실행")
#                     else:
#                         print("과목을 집어넣는 함수 실행")
#                 else:
#                     return False
#
# 요일(colnums)의 리스트가 str으로 모두 채워졌는지의 여부를 검사하는 함수
def com_full_with_string(con, ind_num, remains_day_index):
    i = 0
    while i < len(con):
        while True:
            if (type(df[0][i] == 'str')):
                for j in range(1, ind_num):
                    if (type(df[0][i]) == type(df[j][i])):
                        True
                    else:
                        i += 1
                        break
                del remains_day_index[i]
                i += 1
                break

    return remains_day_index        # 바뀐 remains_day_index


# remains_day=[0,1,2,3,4]=[월,화,수,목,금]



# 횟수 많은 과목을 구하는 용도의 리스트 만들기 함수(리스트 정렬)
def creating_sorted_Lists(subject, subject_times):
   sorted_subject = []             # 서로의 인덱스가 일치하게 내림차순으로 정렬된 두 리스트
   sorted_subject_times = []
   for i in range(len(subject_times)):
        Max = max(subject_times)
        Max_order = subject_times.index(Max)
        sorted_subject.append(subject[Max_order])
        sorted_subject_times.append(Max)
        del subject_times[Max_order]
        del subject[Max_order]

   return sorted_subject, sorted_subject_times


# 과목별 횟수만큼 요일 수를 선택하는 함수
def selecting_day_as_the_number_of_subjects(remains_day_index, sorted_subject, sorted_subject_times):
    # selected_days = [] : selected_days가 요소로 들어가있는 이중리스트
    # selected_day = [] : 각 인덱스에서 뽑힌 요일 값을 저장하는 리스트
    selected_days = []
    for i in range(len(sorted_subject)):
        selected_day = random.sample(remains_day_index, sorted_subject_times[i])
        selected_days.append(selected_day)
    return selected_days


# 요일 중 빈자리에 과목(str)을 넣는 함수
def selecting_empty_space_from_days(remains_day_index, selected_days, selected_day, ind, com_full_with_string):
    for i in range(len(selected_days)):     # 몇 번 반복해야하지?
        for j in range(len(selected_days[i])):
            df.columns[selected_day[j]]     # 여기서 str으로 채워졌는지 여부를 검사해야 하지 않나?

            com_full_with_string
            # if 써야 하고
            // 월요일 열의 행 크기 중 하나 랜덤으로 고르고,
            df.append(row[ind]) = subject[]




# 전에 만들어졌던 시간표와 중복되는 시간표가 만들어지는 경우를 방지하는 함수
def comparing_with_maken_timetable_before():




# 월요일 = 0, 화요일 =1 ...
#         selected_days = {
#             [0, 4, 2, 1],
#             [3, 2, 4],
#             [4, 0, 1]
#             }

#     # 일단 5의 배수일 때 아래 코드를 실행
#     # (몫의 나머지만큼 데이터프레임을 추가로 넣을 필요 없는 코드)
#
#     # respectively_day_subject_array = 각 요일별 과목이 들어갈 2차원 배열형태의 리스트
#     # 아래 코드를 통해 [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None] ...(5개) 만들어짐]
#     row, column = 5, 5
#     # row = int(num)
#     respectively_day_subject_array = [[None for j in range(column)] for i in range(row)]
#     # 과목을 뿌리기 전 None의 상태



# ====================================아래는 참고할 수 있는 코드==============================================

# df[df.colums[j]]
# 요일 중 빈자리 선택하는 함수
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