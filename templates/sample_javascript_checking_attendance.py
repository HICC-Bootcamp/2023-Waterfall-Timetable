import openpyxl as op
result = [1,2,3,4,5]
wb=openpyxl.load_workbook('/templates/manage_attendance.xlsx')      ***엑셀열기
    sheet = wb.active    ***시트열기
    for i in range(30):
      sheet['B+(i+2)'].value= result
*** 셀 B2~B3-에 값 넣기
    wb.save('/templates/manage_attendance.xlsx')