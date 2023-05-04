
# a = -10
# b = -10
# print(a is b)

# a = 100

# if a>0 and (a%2)==0 :
#     print('a is even')

# 7 and 13 13


# 5 and 7 7

# and : 저건이 True/False 로 반환이 됨
#  & : 비트연산자로 작동됨

#  3 & 4 논리연산자가 x -> 비트연산자
# 0011 & 0100 -> 0000 (교집합)

# 논리연산자 : or
# 조건이 True/ False 로 반환이 됨, | : 비트연산자로 작동됨
# print(7 | 13) # 0111|1101  = 15
# print(13 | 7) # 0111|1101 = 15

# a = 34
# b = 4
# if a % b > 3:
#     print("실패")
# elif a % b < 3:
#     print("성공")
# elif a % b == 0:
#     print("무승부")


    

# while True:
#     b = int(input("태어난 년도를 입력하세요"))
#     age = 2023 - b + 1
#     if age <= 26 and age >= 20:
#         print("대학생")
#     elif age < 20 and age >= 17 :
#         print("고등학생")
#     elif age < 17 and age >= 14 :
#         print("중학생")
#     elif age < 14 and age >= 8 :
#         print("초등학생")
#     else: 
#         print("학생이 아닙니다.")



#  양의 정수 하나의 입력 받어 이 정수가 2의 배수인지 3의 배수인지 작성하시오

# a = abs(int(input("숫자를 입력하세요")))

# if a % 2 == 0 and a % 3 == 0:
#     print("2와 3의 배수 입니다.")
# elif a % 2 == 0 and a % 3 != 0:
#     print("2의 배수입니다.")
# elif a % 2 != 0 and a % 3 ==0 :
#     print("3의배수 입니다.")
# else : 
#     print("2와 3 어느 배수도 아닙니다.")

# a = 0
# for i in range(11):
#     a = a+i
# print(a)

# n = int(input("별을 갯수를 입력하세요"))

# for i in range(n):
#     print((i+1) * " " + (n) * "*" )



# for i in range(n):
#     print((i + 1) * "*")

# for i in range(n):
#     print((n-i) * " "+(i + 1) * "*")


# for i in range(n):
#     print((n - i) * "*")


# for i in range(n):
#     print((i) * " " + (n - i) * "*")

# for i in range(1, n+1):
#     print((n-i) * " "+ "*" * (2 * i -1)  + (n-i) * " " )



# x = [3, 6, 9, 20, -7, 5]
# for i in range(0, len(x)):
#     x[i] = x[i]*10
# print(x)

# y = {"math":70, "Science":80, "english":20}

# for key in y:
#     val = y[key]
#     y[key] = y[key]+10
#     print('%s : %d' %(key.val+10))

# import random

# true_value = random.randint(1, 100)

# while True:
#     a = int(input('숫자를 맞춰보세요(1~100)'))
#     if true_value > a :
#         print("숫자가 너무 작습니다.")
#         continue
#     elif true_value < a:
#         print("숫자가 너무 큽니다.")
#         continue
#     elif true_value == a :
#         print("정답입니다")
#         break
# a = list()
# word = ["school", "game", "piano", "science", "hotel", "mountain"]
# for i in range(len(word)):
#     if len(word[i])>= 6 :
#         a.append(word[i])
#     else : pass
# print(a)



# for i in range(1, 10):
#     print(i , "단")
#     for j in range(1, 10):
#         print(i , "*" , j , "=" , i * j)

# a = int(input("숫자를 입력하세요"))
# for i in range(1, a):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, "=", "3과 5의 공배수")
#     elif i % 3 == 0 and i % 5 != 0:
#         print(i, "=", "3의 배수")
#     elif i % 3 != 0 and i % 5 == 0:
#         print(i, "=", "5의 배수")
#     else: print(i)



# # while True:
# #     b = 0
# #     a = input("값을 입력해주세요")
# #     while a == "s" or a == "S":
# #         b =+ a 

    



# mideterm_scoer=[[39, 69, 20, 100, 80], [32, 59, 85, 30, 90], [49, 70, 48, 60, 100]]

# student_score = [0, 0, 0, 0, 0]
# i = 0
# for subject in mideterm_scoer : # kor. math. eng 과목 선택
#     for score in subject: # 과목 선택후
#         student_score[i]+=score #각 학생마다 개별로 교과 점수를 저장
#         i+=1 #학생 index 구분
#     i=0 # 과목이 바뀔 때 학생 인덱스
# else:
#     a,b,c,d,e = student_score # 학년별 점수를 unpacking
#     student_average = [a/3,b/3,c/3,d/3,e/3]
#     print(student_average)


a = [1,2,3,4,5]

def swap_vlaue(x, y):
    temp = x
    x= y
    y = temp

swap_vlaue(a[1],a[2]) 
print(a)   


def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp



swap_offset(1,2) 
print(a)


def swap_offset(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp

swap_offset(a, 1, 2)
print(a)
