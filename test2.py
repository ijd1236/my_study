import pandas as pd

# 엑셀 파일 읽기
file_path = 'C:/Users/iks12/Desktop/11.xlsx'

file_path2 = 'C:/Users/iks12/Desktop/12.xlsx'
df = pd.read_excel(file_path)

# 10번째 행부터 90번째 행까지 선택 (iloc는 0부터 시작하므로 9부터 89까지 선택)
subset_df = df.iloc[1:20]

# "a" 열에서 "bbbb" 값을 가진 행 제외
filtered_df = subset_df[subset_df['a'] != "bb"]

# 결과 확인
print(filtered_df)

# 필요하다면 필터링된 데이터프레임을 새로운 엑셀 파일로 저장
filtered_df.to_excel(file_path2 , index=False)