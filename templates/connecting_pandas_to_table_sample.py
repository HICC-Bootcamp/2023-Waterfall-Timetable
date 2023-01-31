import pandas as pd
from bs4 import BeautifulSoup

# url = table이 나와있는 html파일의 url / table은 출결관리에 사용되는 라디오박스묶음
# df = url로 가서 html파일 전체를 읽은 값
url = 'C:/Users/SAMSUNG/Desktop/Teacherpage_result_containing_javascript.html'
df = pd.read_html(url, encoding="utf-8")

# dfs는 번호를 저장하는 리스트, dfss는 Y/L/N 값을 저장하는 리스트
dfs = []
dfss = []

# dfs리스트에서 번호를 저장, dfs리스트를 Series에 저장
for i in dfs[30]:
    dfs.append[i]
    dfs = pd.Series(dfs)  # Series는 일차원 배열과 비슷한 구조

#
for j in dfss[30]:
    dfss[j] = pd.Series(df[j])

# df[0]를 dataframe으로 만든 결과 : dfs
# dfs[i] = pd.DataFrame(df[i])

# '출석' 열의 결측값을 1로 바꿔야 함_수정해야 할 부분(1/30)
# df['attend'] = df['attend'].fillna(1)
# 열의 이름이 한글이면 어떻게 수정하지?
# dfs.drop(Unnamed:, axis = 1, inplace = True)
# dropna(how="all"))


# dfs의 인덱스 1열_결측값에 1을 집어넣음
# dfs[dfs.columns[1]] =[1, 1, 1, 1, 1, 1]
# dfs[dfs.columns[2]] =[0, 0, 0, 0, 0, 0]
# dfs[dfs.columns[3]] =[0, 0, 0, 0, 0, 0]
# print(dfs)

# to_excel 함수를 통해 dfs를 정해진 엑셀로 보냄 / 절대경로 제대로 쓸 것
dfs.to_excel(excel_writer='C:/Users/SAMSUNG/Desktop/inventors.xlsx')

# 엑셀 -> 웹페이지로 값 전달_김효진
# 엑셀값 훑기, 특정한 숫자가 있다면
# 그 엑셀의 행과 열에 해당하는 html에서의 행과 열을 찾아 checked="checked" 속성 마지막에 추가하기


# 웹페이지(라디오박스) -> 엑셀로 값 전달_오지현
# if문 쓰기 // 웹페이지에서의 라디오박스에 체크되어 있는 속성을 찾기, 체크되어 있으면
# html문서에 해당하는 행과 열에 해당하는 엑셀의 행과 열에 특정한 번호 입력되게 하기.


# 웹페이지(라디오박스) -> 엑셀로 값 전달_오지현_코드 짜보는 중
# 저장 누르면 라디오박스가 (table방식으로) 엑셀에 값을 넣음.
# 테이블의 값을

# page = open("C:/Users/SAMSUNG/Desktop/connecting_pandas_to_table.html", 'rt', encoding = 'utf-8').read()
# soup = BeautifulSoup(page, 'html.parser')

# 만약 html파일에 속성 value='attend'이 포함되어 있다면 열엑셀에 1을 표시해라
# print(soup.find_all(value="attend"))


# 라디오박스 체크버튼과 엑셀 체크버튼 연동하는 프로그램이 있는지

# page = open("C:/Users/SAMSUNG/Desktop/connecting_pandas_to_table.html", 'rt', encoding = 'utf-8').read()
# soup = BeautifulSoup(page, 'html.parser')

# 만약 html파일에 속성 value='attend'이 포함되어 있다면 열엑셀에 1을 표시해라
# print(soup.find_all(value="attend"))

# 값 채우고, 링크 연결,