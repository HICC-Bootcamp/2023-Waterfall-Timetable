import pandas as pd
import openpyxl
filename='manage_attendance.xlsx'
df = pd.read_excel(manage_attendance.xlsx, engine= 'openpyxl')
sheet= wb.worksheets[0]
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
