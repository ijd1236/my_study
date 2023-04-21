# tuple(튜플)형
# 튜플은 elemnet(요소)의 값을 수정할 수 없다
# mutable / immutable
# mutable 수정 가능한 (list, dict,)
# immutable 수정 불가능 (int, float, str, tuple)
# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list)
# my_tuple = (1, 2, 3)
# my_tuple[0] = 5 # erro 튜플형은 수정 불가능
# print(my_typle)
# tuple_1 = ("Hello", "World", "Python")
# t2 = (1, 2, 3, 4, 5)
# t4 = 1, 2, 3

# t6 = tuple_1 + t2
# t7 = t3 * 3 # 수정이 아니라 새로운 연산자를 만든다.
# t7 = t3 * 4

# t3 = (1, 2, "Hello")
# print(t3[2])
# # print(t3[0:2])  (1, 2)
# 인덱싱 슬라이싱도 가능
# 슬라이싱을 하면 묶여져있는 구조(list, dict, tuple) 형태로 가져온다
# print(len(t3))
# t5 = (1, 2, (3, 4, 5))
# print(t5[2][1])

# t8 = (5, 3, 1, 4, 2)
# # tuple  이기 때문에 위치를 바꾸는 sort 로 정렬하지 못 한다
# # 추가도 불가능

# for i in t8:   # 리스트 순서대로 실행된다 5, 3, 1 ,4, 2
#     print(i)









#  2 ~ 9 사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우, 잘못 입력되었다고
# 출력하고 다시 입력 받으세요




# c = (1, 2, 3, 4, 5)
# print(c.index(7))


# for a in range(1, 10):
#     a= int(input("2~9 사이의 숫자를 입력하세요"))
#     if a >= 10 or a <= 1:
#         print("잘못 입력 되었습니다.")
#         continue
#     print("-----", a, "단", "------")
#     for j in range(1, 10):
#         print(a, "*", j, "=", a * j)



# # 2~ 9 사이의 값이 아닐때 True
# if n >= 2 and n <= 10:
#     pass
# if 2 <= n <= 9:
#     pass
# n = int(input("몇 단?"))
# while not 2 <= n <= 9:
#     print("2 ~ 9 사이의 숫자를 입력해주세요")
#     n = int(input("몇단?"))

# for i in range(1, 10): #or (9)
#     print(n, "*", i, "=", n*i)
# for i in rang(9):
    # print(n * (i+1))

# 정수를 입력받고
# 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하세요

# n = int(input("정수:"))
# i = 1
# while True:
#     if i * i >= n:
#         break
#     answer = i * i
#     i += 1
# print(answer)
    
# n = int(input("정수:"))
# for i in range(n):
#     if i * i >= n:
#         break
#     answer = i * i
# print(answer)

#  [1, 2, 3, 4, 5]
#  [10, 20, 30, 40, 50]
#  [532, 5941, 54682, 58, ,5]
#  3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]

# for i in range(5):
#     print(a[i] + b[i] + c[i])

# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용 가능한 iterable을 반환한다.

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]
# # for x, y, z in zip(a, b, c):
# #     print(x + y + z)
# x = zip(a, b, c)
# print(x, type(x))
# print(list(x))

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]
# i=0
# while i < 5:
#     print(a[i] + b[i] + c[i])
#     i += 1


# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
# 단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝이라고 출력하세요
# a = int(input("입력하시오"))
# for i in range(1, a + 1):
#     answer = i
#     for j in str(i):
#         if int(j) % 3 == 0 and j != "0":
#             answer = "짝"
#             break
#     print(answer)



#  정수를 입력받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나눴을 때 나머지가 0으로 떨어지게 하는 수

# a= int(input("정수를 입력하세요"))

# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i)

# for i in range(a): # 0 ~ n-1
#     if a % (i+1) == 0:
#         print(i+1)

# i = 1
# while i <= a:
#     if a % i == 0:
#         print(i)
#     i += 1



t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)