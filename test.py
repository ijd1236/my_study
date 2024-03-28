import subprocess

# 실행할 bat 파일들의 리스트
bat_files = ["aa.bat", "bb.bat"]

# 실행할 횟수 설정
repeat_count = 3

# 각각의 bat 파일을 설정된 횟수만큼 실행
for _ in range(repeat_count):
    for bat_file in bat_files:
        subprocess.call([bat_file])





# @echo off

# set /p batFile="실행할 bat 파일의 이름을 입력하세요 (확장자 포함): "
# set /p repeat="반복할 횟수를 입력하세요: "

# rem 입력한 bat 파일을 실행합니다.
# if exist "%batFile%" (
#     rem 지정된 횟수만큼 반복 실행합니다.
#     for /l %%i in (1, 1, %repeat%) do (
#         echo 실행 중: %batFile%
#         call %batFile%
#     )
# ) else (
#     echo 입력한 이름의 bat 파일이 존재하지 않습니다.
# )

# echo 모든 작업이 완료되었습니다.
# pause
