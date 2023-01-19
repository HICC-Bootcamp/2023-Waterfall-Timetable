
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def initial():
    return render_template('initial page_1.html')

@app.route('/Teacherpage/1/')
def teacher():
    return render_template('Teacherpage_1.html')

@app.route('/3/')
def teacher_2():
    return render_template('Teacherpage_2.html')
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

