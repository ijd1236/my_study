import os

# 디렉토리 경로
directory_path = 'your_directory_path'

# 변수 초기화
a = None
b = None

# 디렉토리 내의 파일 및 디렉토리 목록 가져오기
files_and_directories = os.listdir(directory_path)

# 디렉토리 내의 zip 파일 필터링 및 속성 출력
for item in files_and_directories:
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path) and item.lower().endswith('.zip'):
        # zip 파일인 경우만 처리
        if len(item) >= 42 and item[41] == '1':
            # 이름의 42번째 문자가 '1'인 경우
            zip_size = os.path.getsize(item_path)  # 파일 크기 가져오기
            a = item  # 파일 이름 저장
            b = zip_size  # 파일 크기 저장
            break  # 조건을 만족하는 파일을 찾았으므로 루프 종료

# 결과 출력
if a is not None and b is not None:
    print(f"파일 이름: {a}, 크기: {b} bytes")
else:
    print("해당 조건을 만족하는 파일을 찾지 못했습니다.")
