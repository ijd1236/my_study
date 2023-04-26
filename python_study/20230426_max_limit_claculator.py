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
    pass

maxlimitCalculator = MaxLimitCalculator()

try:
    maxlimitCalculator.div(5, 0)             
except ZeroDivisionError:
    print("0입력하지마")

