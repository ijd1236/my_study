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


