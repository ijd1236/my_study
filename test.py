import os
import re
import json

# SQL 파일 내의 모든 값들을 수정하는 함수
def modify_values_in_file(file_path, target_key, replacement):
    with open(file_path, 'r') as file:
        sql_content = file.read()

        # JSON 데이터를 수정합니다.
        modified_content = modify_json_data(sql_content, target_key, replacement)

        # 변경된 내용을 파일에 씁니다.
        with open(file_path, 'w') as file:
            file.write(modified_content)

# JSON 데이터를 수정하는 함수
def modify_json_data(sql_content, target_key, replacement):
    # JSON 데이터를 파싱하여 수정합니다.
    data = json.loads(sql_content)
    if target_key in data:
        data[target_key] = replacement
    modified_content = json.dumps(data)
    return modified_content

# SQL 파일이 들어있는 폴더 경로
folder_path = '/경로/폴더'

# 수정할 키, 대체할 값
target_key = 'va'
replacement = '원하는 값'

# 폴더 내의 모든 파일을 확인합니다.
for file_name in os.listdir(folder_path):
    if file_name.endswith('.sql'):
        file_path = os.path.join(folder_path, file_name)
        modify_values_in_file(file_path, target_key, replacement)

print('작업 완료')
