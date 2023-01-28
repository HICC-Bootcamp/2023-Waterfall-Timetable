
from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)


@app.route('/')
def initial():
    return render_template('initialpage_1.html')


@app.route('/Teacherpage/1/',)
def teacher():
    return render_template('Teacherpage_1.html')


@app.route('/Teacherpage/2/', methods=["GET", "POST"])
def teacher_2():
    if request.method == "POST":
        subject_select = request.form.get("subject")

        return render_template('Teacherpage_2.html', subject_select = subject_select)
    return render_template('Teacherpage_2.html')


@app.route('/Teacherpage/3/', methods=["GET", "POST"])
def teacher_3():
    return render_template('Teacherpage_3.html')


@app.route('/Teacherpage/4/', methods=["GET", "POST"])
def teacher_4():
    if request.method == "POST":
        class_select = request.form.get("class")

        period = list()
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])

        return render_template('Teacherpage_manageClass.html', rows=period, class_select=class_select)

    return render_template('Teacherpage_manageClass.html')


@app.route('/studentpage/1/', methods=["GET", "POST"])
def student():
    return render_template('studentpage_1.html')


@app.route('/studentpage/2/', methods=["GET", "POST"])
def student2():
    if request.method == "POST":
        class_select = request.form.get("class")

        period = list()
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])
        period.append([0, 0, 0, 0, 1])

        return render_template('studentpage_2.html', rows=period, class_select=class_select)
    return render_template('studentpage_2.html')


@app.route('/manager/', methods=["GET", "POST"])
def manager():
    return render_template('manager.html')


@app.route('/manager_result/', methods=["GET", "POST"])
def manager_result():
    if request.method == "POST":
        class_number = request.form.get("class_number")
        # class_number는 직접 시도해보세요ㅎ 테이블을 여러개 만들면됩니다.

        korean1 = int(request.form.get("korean1_class"))
        korean2 = int(request.form.get("korean2_class"))
        math1 = int(request.form.get("math1_class"))
        math2 = int(request.form.get("math2_class"))
        english = int(request.form.get("english_class"))
        social = int(request.form.get("social_class"))
        science = int(request.form.get("science_class"))
        physical = int(request.form.get("physical_class"))

        period = list()
        period.append([0, 0, 0, 0, korean1])
        period.append([0, 0, 0, 0, korean2])
        period.append([0, 0, 0, 0, math1])
        period.append([0, 0, 0, 0, math2])
        period.append([0, 0, 0, 0, english])
        period.append([0, 0, 0, 0, social])
        period.append([0, 0, 0, 0, science])
        period.append([0, 0, 0, 0, physical])

        return render_template('manager_result.html', rows=period)

    return render_template('manager_result.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="9999")





####엑셀 파일 생성
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws_new = wb.create_sheet()
ws.title = "class1"
ws_new.title = "class2"
sheet3 = wb.create_sheet('class3')
sheet4 = wb.create_sheet('class4')
sheet5 = wb.create_sheet('class5')
sheet6 = wb.create_sheet('class6')
sheet7 = wb.create_sheet('class7')
sheet8 = wb.create_sheet('class8')
wb.save("timetable.xlsx")

from openpyxl import load_workbook

wb = load_workbook("timetable.xlsx")

ws = wb["class1"]

