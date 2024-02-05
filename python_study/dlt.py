import os
import dlt

def read_dlt_file(file_path):
    with dlt.File(file_path) as file:
        for message in file:
            # 각 메시지의 내용을 처리하거나 출력합니다.
            print(message)

if __name__ == "__main__":
    dlt_file_path = "bbb.dlt"
    read_dlt_file(dlt_file_path)