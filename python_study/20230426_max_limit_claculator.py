# my_calculator 모듈의 MyCalculator 클래스를 상속받아서
# MaxLimitCalculator 클래스를 정의하세요
# add, sub, bul, div 메소드를 사용하여 
# 더하기, 빼기, 곱하기, 나누기를 할 수 있다
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다,.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고 
# 100이하의 값을 입력하도록 안내 메시지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 
# 100이하의 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다.


from my_calculator import MyCalculator

class MaxLimitCalculator(MyCalculator):
    def add(self, a, b):
        if a > 100 or b > 100:
            print("100보다 작은  수를 입력하세요")
        else : 
            result = a + b
            if result > 100 :
                print("계산괄과가 100보다 작아야합니다")
            else:
                print(f"{a} + {b} = {a+b}")
    def sub(self, a, b):
        if a > 100 or b > 100:
            print("100보다 작은  수를 입력하세요")
        else : 
            result = a - b
            if result > 100 :
                print("계산괄과가 100보다 작아야합니다")
            else:
                print(f"{a} - {b} = {a-b}")        
    def mul(self, a, b):
        if a > 100 or b > 100:
            print("100보다 작은  수를 입력하세요")
        else : 
            result = a * b
            if result > 100 :
                print("계산괄과가 100보다 작아야합니다")
            else:
                print(f"{a} * {b} = {a*b}")
    def div(self, a, b):
        if a > 100 or b > 100:
            print("100보다 작은  수를 입력하세요")
        else:
            try : 
                result = a / b 
            except ZeroDivisionError:
                print("0으로 나누지 마세요")    
            if result > 100 :
                    print("계산괄과가 100보다 작아야합니다")
            else:
                print(f"{a} / {b} = {a/b}")



maxlimitCalculator = MaxLimitCalculator()

maxlimitCalculator.div(101, 100)


# try:
#     maxlimitCalculator.div(99, 99)             
# except ZeroDivisionError:
#     print("0입력하지마")  

