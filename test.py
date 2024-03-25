import os
import re
import json

# SQL 파일 내에서 특정 테이블의 JSON 데이터를 수정하는 함수
def modify_json_in_table(file_path, target_table, target_key, replacement):
    with open(file_path, 'r') as file:
        sql_content = file.read()

        # 특정 테이블의 내용을 찾습니다.
        table_content = find_table_content(sql_content, target_table)

        # 찾은 내용에서 원하는 값을 수정합니다.
        if table_content:
            modified_table_content = modify_json_in_content(table_content, target_key, replacement)
            modified_content = sql_content.replace(table_content, modified_table_content)

            # 변경된 내용을 파일에 씁니다.
            with open(file_path, 'w') as file:
                file.write(modified_content)
        else:
            print(f"{target_table} 테이블을 찾을 수 없습니다.")

# SQL 파일 내에서 특정 테이블의 내용을 찾는 함수
def find_table_content(sql_content, target_table):
    table_pattern = re.compile(rf'CREATE\s+TABLE\s+{target_table}\s*\((.*?)\)', re.DOTALL)
    match = table_pattern.search(sql_content)
    if match:
        return match.group()
    return None

# 특정 테이블의 JSON 데이터를 수정하는 함수
def modify_json_in_content(table_content, target_key, replacement):
    # JSON 데이터를 파싱하여 수정합니다.
    data = json.loads(table_content)
    if target_key in data:
        data[target_key] = replacement
    modified_content = json.dumps(data)
    return modified_content

# SQL 파일이 들어있는 폴더 경로
folder_path = '/경로/폴더'

# 수정할 테이블 이름, 수정할 키, 대체할 값
target_table = 'aa'
target_key = 'va'
replacement = '원하는 값'

# 폴더 내의 모든 파일을 확인합니다.
for file_name in os.listdir(folder_path):
    if file_name.endswith('.sql'):
        file_path = os.path.join(folder_path, file_name)
        modify_json_in_table(file_path, target_table, target_key, replacement)

print('작업 완료')
