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

if Total_times % 5 == 0:
    ind_num = Total_times // 5
    col = ["월", "화", "수", "목", "금"]
    ind = []
    for i in range(1, ind_num + 1):
        ind.append(i)
    con = []

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
