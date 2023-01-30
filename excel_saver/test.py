import pandas as pd
import openpyxl
<<<<<<< HEAD:excel_saver/test.py
filename='manage_attendance.xlsx'
df = pd.read_excel(manage_attendance.xlsx, engine= 'openpyxl')

=======
filename = 'C:/Users/user/Desktop/올빼미/excel_saver/manage_attendance.xlsx'
<<<<<<< HEAD
wb = openpyxl.load_workbook(manage_attendance,xlsx)
=======
wb = openpyxl.load_workbook(filename)
>>>>>>> 813f8af (manager_result 주석 처리)
>>>>>>> cdf5fb74b8cc01709255af7d804a0af3f7d098cf:templates/test.py
sheet=wb.worksheets[0]
data = []
for row in sheet.rows:
    data .append([
        row[0],value,
        row[1], value,
        row[2], value,
        row[3], value,
        row[4], value,
    ])
    print(data)
