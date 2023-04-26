# # 계산기 만들기
# # 기능 : 두 정수의 사칙연산(+, -, *, /)
# # add(), sub(), mul(), dic() 함수 정의 input() 함수를 활용하여
# #  정수 2개, 사칙연산 선택을 입력받은 후
# #  계산 결과를 print 한다.
# # 계산식과 결과를 calculator_result.txt파일에 기록한다
# # 사용자가 'q' 를 입력하면 종료한다.


# def add(a, b):
#     result = str(a)+ " + "+str(b)+" = "+str(a+b)
#     print(result)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8")as f:
#         f.write(result)
#         f.write("\n")


# def sub(a, b):
#     result = str(a)+ " - "+str(b)+" = "+str(a-b)
#     print(result)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8")as f:
#         f.write(result)
#         f.write("\n")

# def mul(a, b):
#     result = str(a)+ " * "+str(b)+" = "+str(a*b)
#     print(result)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8")as f:
#         f.write(result)
#         f.write("\n")

# def dic(a, b):
#     result = str(a)+ " / "+str(b)+" = "+str(a/b)
#     print(result)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8")as f:
#         f.write(result)
#         f.write("\n")


# while True:
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 계산를 입력하세요")
#     if operator == 'q':
#         break  
#     a = int(input("정수 1: "))
#     b = int(input("정수 2: "))
#     if operator == "1" :
#         add(a, b)

#     elif operator == "2" :
#         sub(a, b)

#     elif operator == "3":
#         mul(a, b)
  
#     elif operator == "4":
#         dic(a, b)



# Mycalculator 클래스로 만들어보ㅔㅅ요
# add, sub, mul, div 메소드


class MyCalculator:
    def __init__(self):
        pass
    def add(self, a, b):
        print(f"{a} + {b}  = {a+b}")
    def sub(self, a, b):
        print(f"{a} - {b}  = {a-b}")
    def mul(self, a, b):
        print(f"{a} * {b}  = {a*b}")
    def div(self, a, b):
        print(f"{a} / {b}  = {a/b}")
    



if __name__ == "__main__":       
    while True:
        my_calculator =  MyCalculator()
        print("""
        계산기
        1: +
        2: -
        3: *
        4: /
        q: 종료
        """)
        operator = input("원하는 계산를 입력하세요")
        if operator == 'q':
            break  
        a = int(input("정수 1: "))
        b = int(input("정수 2: "))
        if operator == "1" :
            my_calculator.add(a, b)

        elif operator == "2" :
            my_calculator.sub(a, b)

        elif operator == "3":
            my_calculator.mul(a, b)
    
        elif operator == "4":
            my_calculator.dic(a, b)
        else:
            print("잘못 입력했습니다")


