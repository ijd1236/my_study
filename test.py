import os
import re
import json

# SQL 파일 내에서 특정 테이블의 특정 열에 있는 JSON 데이터를 수정하는 함수
def modify_value_in_table_column(file_path, target_table, target_column, target_key, replacement):
    with open(file_path, 'r') as file:
        sql_content = file.read()

        # 특정 테이블의 특정 열에 있는 내용을 찾습니다.
        table_content = find_table_column_content(sql_content, target_table, target_column)

        # 찾은 내용에서 원하는 값을 수정합니다.
        if table_content:
            modified_table_content = modify_json_in_column(table_content, target_key, replacement)
            modified_content = sql_content.replace(table_content, modified_table_content)

            # 변경된 내용을 파일에 씁니다.
            with open(file_path, 'w') as file:
                file.write(modified_content)
        else:
            print(f"{target_table} 테이블의 {target_column} 열을 찾을 수 없습니다.")

# SQL 파일 내에서 특정 테이블의 특정 열에 있는 내용을 찾는 함수
def find_table_column_content(sql_content, target_table, target_column):
    column_pattern = re.compile(rf'CREATE\s+TABLE\s+{target_table}\s*\((.*?)\)', re.DOTALL)
    match = column_pattern.search(sql_content)
    if match:
        table_definition = match.group(1)
        column_pattern = re.compile(rf'"{target_column}"\s+\w+\s*.*?,', re.DOTALL)
        column_match = column_pattern.search(table_definition)
        if column_match:
            column_content = column_match.group()
            return column_content
    return None

# 특정 열에 있는 JSON 데이터를 수정하는 함수
def modify_json_in_column(column_content, target_key, replacement):
    # JSON 데이터를 파싱하여 수정합니다.
    data = json.loads(column_content)
    if target_key in data:
        data[target_key] = replacement
    modified_content = json.dumps(data)
    return modified_content

# SQL 파일이 들어있는 폴더 경로
folder_path = '/경로/폴더'

# 수정할 테이블 이름, 특정 열 이름, 수정할 키, 대체할 값
target_table = 'aa'
target_column = 'bb'
target_key = 'va'
replacement = '원하는 값'

# 폴더 내의 모든 파일을 확인합니다.
for file_name in os.listdir(folder_path):
    if file_name.endswith('.sql'):
        file_path = os.path.join(folder_path, file_name)
        modify_value_in_table_column(file_path, target_table, target_column, target_key, replacement)

print('작업 완료')






# 위의 코드는 주어진 SQL 파일 내에서 특정 테이블의 특정 열에 있는 JSON 형식의 데이터를 수정하는 파이썬 코드입니다. 각 부분을 자세히 설명하겠습니다.

# modify_value_in_table_column 함수:

# 이 함수는 SQL 파일 내에서 특정 테이블의 특정 열에 있는 JSON 데이터를 수정합니다.
# 인자로는 SQL 파일 경로(file_path), 대상 테이블 이름(target_table), 대상 열 이름(target_column), 수정할 키(target_key), 대체할 값(replacement)을 받습니다.
# 함수는 SQL 파일을 열고, 대상 테이블의 특정 열에 있는 내용을 찾은 후 해당 JSON 데이터를 수정하고, 수정된 내용을 다시 파일에 씁니다.
# find_table_column_content 함수:

# 이 함수는 SQL 파일 내에서 특정 테이블의 특정 열에 있는 내용을 찾습니다.
# re.compile() 함수를 사용하여 정규 표현식 패턴을 설정하고, SQL 파일 내에서 해당 패턴과 일치하는 부분을 검색합니다.
# 찾은 내용은 해당 테이블의 정의에서 대상 열의 내용을 나타내며, 이를 반환합니다.
# modify_json_in_column 함수:

# 이 함수는 특정 열에 있는 JSON 데이터를 수정합니다.
# json.loads() 함수를 사용하여 JSON 형식의 문자열을 파이썬 객체로 변환한 후, 대상 키를 사용하여 해당 값을 수정합니다.
# 수정된 객체를 다시 JSON 형식의 문자열로 변환한 후 반환합니다.
# 코드 실행 부분:

# 주어진 폴더 내의 모든 SQL 파일을 확인하고, 각 파일에 대해 modify_value_in_table_column 함수를 호출하여 JSON 데이터를 수정합니다.
# 수정된 내용이 파일에 씌여집니다.
# 이 코드는 SQL 파일에서 특정 테이블의 특정 열에 있는 JSON 데이터를 수정하기 위해 사용됩니다. 예를 들어, target_table이 "aa", target_column이 "bb"이고 해당 열의 데이터가 JSON 형식으로 되어 있을 때, 이 코드는 해당 JSON 데이터에서 target_key가 "va"인 값을 replacement 값으로 수정합니다.
