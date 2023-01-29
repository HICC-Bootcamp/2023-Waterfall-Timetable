import pandas as pd
import openpyxl
filename = 'C:/Users/user/Desktop/올빼미/excel_saver/manage_attendance.xlsx'
wb = openpyxl.load_workbook(manage_attendance)
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
