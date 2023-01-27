
from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)

@app.route('/')
def initial():
    return render_template('initial page_1.html')

@app.route('/Teacherpage/1/')
def teacher():
    return render_template('Teacherpage_1.html')

@app.route('/Teacherpage/2/')
def teacher_2():
    return render_template('Teacherpage_2.html')
@app.route('/Teacherpage/4/')
def teacher_4():
    return render_template('Teacherpage_manageClass.html')
@app.route('/studentpage/1/')
def student():
    return render_template('studentpage_1.html')
@app.route('/studentpage/2/')
def student2():
    return render_template('studentpage_2.html')

@app.route('/manager/')
def manager():
    return render_template('manager.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="9999")

#####엑셀파일 생성
import openpyxl
wb = openpyxl.Workbook()

wb.active.title = "시간표 생성1"
wb.create_sheet("시간표 생성2")

new_filename = 'C:/Users/user/Desktop/올빼미/excel saver/excel.xlsx'

wb.save(new_filename)