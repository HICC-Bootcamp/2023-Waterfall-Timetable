
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random
import copy


app = Flask(__name__)

@app.route('/manager_result/', methods=["GET", "POST"])
def manager_result():
    if request.method == "POST":
        class_number = int(request.form.get("class_number"))#학급의 개수를 post로 받아서 시간표를 반복생성할때 사용
        all_timetable = []
        subject = ["국어1", "국어2", "수학1","수학2", "영어", "사회","과학", "체육"] #과목명 리스트
        subject_times = [] #과목별 수업시수 리스트 (드롭다운으로 받아서 정수로 subject_times 리스트에 저장)

        korean1 = int(request.form.get("korean1_class"))
        korean2 = int(request.form.get("korean2_class"))
        math1 = int(request.form.get("math1_class"))
        math2 = int(request.form.get("math2_class"))
        english = int(request.form.get("english_class"))
        social = int(request.form.get("social_class"))
        science = int(request.form.get("science_class"))
        physical = int(request.form.get("physical_class"))
        subject_times.extend([korean1, korean2, math1, math2, english, social, science, physical])

        total_times = korean1+korean2+math1+math2+english+social+science+physical  #총합시간

        if total_times % 5 == 0:
            ind_num = total_times // 5
            col = ["월", "화", "수", "목", "금"]
            ind = []
            for i in range(1, ind_num + 1):
                ind.append(i)
            con = []
            for i in range(int(class_number)):  # 학급 수 만큼 테이블 생성
                df = pd.DataFrame(con, columns=col, index=ind)
                all_timetable.append(df)
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
                                if all_timetable[m].iloc[l, j] == class_subject[l]:
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
        a=all_timetable[0]


        return render_template('manager_result.html', class_number=class_number, class_list=class_list)

    return render_template('manager_result.html')




if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="9999")





