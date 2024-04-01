import os

# 디렉토리 경로
directory_path = 'your_directory_path'

# 디렉토리 내의 파일 및 디렉토리 목록 가져오기
files_and_directories = os.listdir(directory_path)

# 디렉토리 내의 zip 파일 필터링 및 속성 출력
for item in files_and_directories:
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path) and item.lower().endswith('.zip'):
        # zip 파일인 경우만 처리
        zip_size = os.path.getsize(item_path)  # 파일 크기 가져오기
        print(f"파일 이름: {item}, 크기: {zip_size} bytes")
