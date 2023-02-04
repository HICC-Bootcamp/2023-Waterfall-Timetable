from flask import Flask, render_template, request,jsonify,json
import pandas as pd
import openpyxl
import copy
import random

app = Flask(__name__)

num_of_class = 0

@app.route('/')
def initial():
    return render_template('initialpage_1.html')


@app.route('/Teacherpage/1/', )
def teacher():
    return render_template('Teacherpage_1.html')


@app.route('/Teacherpage/2/', methods=["GET", "POST"])
def teacher_2():
    if request.method == "POST":
        subject_select = request.form.get("subject")
        df = pd.read_excel('ALL_class.xlsx', sheet_name=None)

        class_table = list()
        for class_ in range(0, num_of_class):
            df[f'{class_ + 1}반'] = df[f'{class_ + 1}반'].drop(df[f'{class_ + 1}반'].columns[0], axis=1)
            class_table.append(df[f'{class_+1}반'].values.tolist())

        korean1_table = [[" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " "]]

        for i in range(0,num_of_class):
            for j in range(0, 8):
                for k in range(0, 5):
                    if class_table[i][j][k] == subject_select:
                        korean1_table[j][k] = f'{i+1}반'

        print(korean1_table)

        return render_template('Teacherpage_2.html', subject_select=subject_select, class_table=korean1_table)
    return render_template('Teacherpage_2.html')


@app.route('/Teacherpage/3/', methods=["GET", "POST"])
def teacher_3():
    return render_template('Teacherpage_3.html', num_of_class=num_of_class)


@app.route('/Teacherpage/4/', methods=["GET", "POST"])
def teacher_4():
    if request.method == "POST":
        class_ind = request.form.get("class_ind")
        df_list = []
        df = pd.read_excel('ALL_class.xlsx', sheet_name=None)
        df_list = df[f'{class_ind}반'].values.tolist()


        return render_template('Teacherpage_manageClass.html',df_list=df_list)

    return render_template('Teacherpage_manageClass.html')


@app.route('/studentpage/1/', methods=["GET", "POST"])
def student():
    return render_template('studentpage_1.html', num_of_class=num_of_class)


@app.route('/studentpage/2/', methods=["GET", "POST"])
def student2():
    if request.method == "POST":
        class_ind=request.form.get("class_ind")
        df_list = []
        df = pd.read_excel('ALL_class.xlsx', sheet_name=None)
        df_list = df[f'{class_ind}반'].values.tolist()

        return render_template('studentpage_2.html', df_list=df_list)
    return render_template('studentpage_2.html')


@app.route('/manager/', methods=["GET", "POST"])
def manager():
    return render_template('manager.html')


@app.route('/manager_result/', methods=["GET", "POST"])
def manager_result():
    if request.method == "POST":
        class_number = int(request.form.get("class_number"))#학급의 개수를 post로 받아서 시간표를 반복생성할때 사용
        global num_of_class
        num_of_class = class_number

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
        i=0
        while i < len(subject):
            if subject_times[i]==0:
                del subject[i]
                del subject_times[i]
                continue
            else:
                i+=1


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
                                if all_timetable[m].iloc[l,j] == class_subject[l]:
                                    class_subject = []
                                    random_subjects = random.sample(subject_copy, ind_num)
                                    class_subject.extend(random_subjects)
                                    l=0
                                    m=0
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
        class_time=[]
        for i in range(0,class_number) :
            class_time.append(all_timetable[i].values.tolist())


        with pd.ExcelWriter('ALL_class.xlsx') as writer:
            if class_number==1:
                all_timetable[0].to_excel(writer, sheet_name='1반')

            elif class_number==2:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')

            elif class_number == 3:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')

            elif class_number == 4:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')
                all_timetable[3].to_excel(writer, sheet_name='4반')

            elif class_number == 5:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')
                all_timetable[3].to_excel(writer, sheet_name='4반')
                all_timetable[4].to_excel(writer, sheet_name='5반')

            elif class_number == 6:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')
                all_timetable[3].to_excel(writer, sheet_name='4반')
                all_timetable[4].to_excel(writer, sheet_name='5반')
                all_timetable[5].to_excel(writer, sheet_name='6반')

            elif class_number == 7:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')
                all_timetable[3].to_excel(writer, sheet_name='4반')
                all_timetable[4].to_excel(writer, sheet_name='5반')
                all_timetable[5].to_excel(writer, sheet_name='6반')
                all_timetable[6].to_excel(writer, sheet_name='7반')

            elif class_number == 8:
                all_timetable[0].to_excel(writer, sheet_name='1반')
                all_timetable[1].to_excel(writer, sheet_name='2반')
                all_timetable[2].to_excel(writer, sheet_name='3반')
                all_timetable[3].to_excel(writer, sheet_name='4반')
                all_timetable[4].to_excel(writer, sheet_name='5반')
                all_timetable[5].to_excel(writer, sheet_name='6반')
                all_timetable[6].to_excel(writer, sheet_name='7반')
                all_timetable[7].to_excel(writer, sheet_name='8반')



        return render_template('manager_result.html', class_number=class_number, class_time=class_time)

    return render_template('manager_result.html')


@app.route('/Teacher/result/', methods=["GET", "POST"])
def teacherresult():
    df = pd.read_excel('./templates/manage_attendance.xlsx')
    data = []
    for i in range(30):
        data.append(df.loc[i, "출결"])
    print(data)
    return render_template('Teacher_result.html', data=data)


@app.route('/myfunction', methods=["POST"])
def myfunction():
    data = json.loads(request.data)
    data.get('submit_result')
    list_ = data['submit_result']
    print(list_)
    wb = openpyxl.load_workbook('./templates/manage_attendance.xlsx')
    sheet = wb.active
    for i in range(30):
        sheet.cell(row=i+2, column=2).value = list_[i]
    wb.save('./templates/manage_attendance.xlsx')
    return jsonify(response=list_)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="9999")


import os

def checking_existence_of_timetable():
    context = False
    path = "/ALL_class.xlsx"
    if(os.path.isfile(path)):
# "현재 디렉토리에 엑셀파일이 있는지 없는지의 여부를 따지는 코드가 없다."
        context = True
    return render_template('Teacherpage_1.html', context=context), render_template('studentpage_1.html', context=context)

