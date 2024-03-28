import subprocess

# 실행할 bat 파일들의 리스트
bat_files = ["aa.bat", "bb.bat"]

# 실행할 횟수 설정
repeat_count = 3

# 각각의 bat 파일을 설정된 횟수만큼 실행
for _ in range(repeat_count):
    for bat_file in bat_files:
        subprocess.call([bat_file])