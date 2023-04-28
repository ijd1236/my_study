# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와, 5의 배수를 모두 더한 합을 
# 반환하는 함수 
# 함수 이름 : sum_3_5

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result
# a = sum_3_5(50)
# print(a)


# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0:
#             result += i
#         elif i % 5 ==0 :
#             result += i
#     return result

# a = sum_3_5(50)
# print(a)

# 정육면체 주사위 2개가 있다
#  2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 
# 모두 print하는 함수를 정의하세요
# 함수 이름 : double_dice
# 1, 2
# 6, 3

# def double_dice ():
#     for i in range(1, 7): #1 ~6
#         for j in range(1, 7) :
#             print(i, j)


# def double_dice():
#     i = 1
#     while i < 7 :
#         j = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1     


# double_dice()
    
#  두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요
#  함수 이름 : get_diff

# def get_diff(a, b):
#     result = abs(a-b)
#     return result

# def get_diff(a, b):
#     result = a - b
#     if a> b: 
#         result = a- b
#     else:
#         result = b - a
#     return result    


# a = get_diff(4, 4)
# print(a)


#  가장 큰 수를 만드는 함수
#  함수에 입력된 5개 정수를 사용하여 만들 수 있는(0~9)
#  가장 큰 수를 반환하는 함수를 정의하세요
#  함수 이름 : get_biggest
# 파라미터 : a, b, c, d, e
# 반환값 : result


# def get_biggest(a, b, c, d, e):
    
#     numbers = [a, b, c, d, e] 
#     numbers.sort()
#     result = 0
#     for i in range(len(numbers)): # 0 ~4
#         result += numbers[i] * (10 ** i)
#     return result
  


# a = get_biggest(5, 6, 7, 8, 9) 
# print(a)


# 별 찍기2
# 정수를 함수에 입력하여 호출하면 해당 정수의 줄의 별을 화면에 출력한다.
# 함수 이름 : print_stars2
"""
출력 결과
n -> 1
*
n-> 4
   *
  **
 ***
****
"""

def print_stars2 (n):
    for i in range(n):
#        print(" " * (n - (i+1)) + (i + 1) * "*")
        print(" " * (n - (i+1)) + (i + 1) * "*")


# print_stars2(10)






# def print_sters(n):
#     for i in range(n):
#         print((i + 1) * "*")

