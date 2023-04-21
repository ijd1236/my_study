# while 반복문
"""
while 조건:
    반복할 코드

"""
# 조건이 참인 경우에 코드를 계속 반복

# n = 1
# while n <= 10:
#     print(n)
#     n += 1 #n = n+1

# += 연산자 
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
#  - , * . / 등 모든 연산자 적용 가능

# s1 = "안녕"
# s1 += "하세요" # 문자열에도 적용 가능하다
# print(s1) = 안녕하세요


# while 반복문을 활용하여 10부터 1까지 출력하세요

# n = 10

# while n >= 1:  # whil n > 0
#     print(n)
#     n -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price:  #while money - price >=0: 
#     print("커피를 구매했습니다")
#     money -= price 
#     coffee -= 1
#     print("남은 커피 :", coffee)
#     if coffee == 0:
#         break


# break 
# 반복문을 즉시 종료한다.

# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.

# a = 1

# while  a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1

#  continue
#  반복문의 제일 처음으로 돌아감
# b = 0
# while b < 10:
#     b += 1        
#     if b % 2 == 0:
#         continue
#     print(b)

C

# 무한 반복문
# 무한 루프
#  조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다
#  ctrl + c 강제 종료

# while True:
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#         break

#  무한반복문으로 계산기 만들기
#  +, -, *, / 계산
#  2개의 수를 계산 a + b

# while True:
#     print("""
#     계산기
#     ======
#     1. 더하기(+)
#     2. 뻬기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)
#     operater = input("계산을 선택하세요 : ")
    # if operater == "1":
    #     print("정답: " + (str(input()) + str(input()))) 
    # if operater == "2":
    #     print(int(input()) - int(input()))   
    # if operater == "3":
    #     print(int(input()) * int(input()))
    # if operater == "4":
    #     print(int(input()) / int(input())) 
    # if operater == "q":
    #     break

    # a = int(input("숫자를 입력하세요."))
    # b = int(input("숫자를 입력하세요."))
    # if operater == "1":
    #     print(a, "+", b, "=", a+b)
    # if operater == "2":
    #     print(a, "-", b, "=", a-b)
    # if operater == "3":
    #     print(a, "*", b, "=", a*b)    
    # if operater == "4":
    #     print(a, "/", b, "=", a/b)
    # if operater == "q":
    #     break

# 사용자가 가지고 있는 돈을 입력 받는다.
#  구매할 수 있는 커피의 개수와 잔돈을 출력한다
#  구매할 수 있는 음료수의 개수와 잔돈을 출력한다
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다
# 커피는 500원 음료수는 700원 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈"))
# while idx < len(prices):
# # while idx < 3:
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1

# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를 
# 정수형으로 입력받으세요.


# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수:"))
#     scores.append(score)
#     n += 1
# print(scores)

# while 반복문을 사용하여
# 구구단 2단을 출력하세요

# n = 1
# while n < 10:
#     print("2 *", n, "=", 2*n)
#     n += 1




