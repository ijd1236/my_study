import os
import re

# SQL 파일 내에서 특정 값들을 수정하는 함수
def modify_values_in_file(file_path, target_key, replacement):
    with open(file_path, 'r') as file:
        sql_content = file.read()

        # 특정 값을 찾아 치환합니다.
        modified_content = modify_values(sql_content, target_key, replacement)

        # 변경된 내용을 파일에 씁니다.
        with open(file_path, 'w') as file:
            file.write(modified_content)

# 특정 값을 찾아 치환하는 함수
def modify_values(sql_content, target_key, replacement):
    # 특정 키와 대체 값으로 치환합니다.
    modified_content = sql_content.replace(target_key, replacement)
    return modified_content

# SQL 파일이 들어있는 폴더 경로
folder_path = '/경로/폴더'

# 수정할 키, 대체할 값
target_key = '원래값'
replacement = '변경할값'

# 폴더 내의 모든 파일을 확인합니다.
for file_name in os.listdir(folder_path):
    if file_name.endswith('.sql'):
        file_path = os.path.join(folder_path, file_name)
        modify_values_in_file(file_path, target_key, replacement)

print('작업 완료')
