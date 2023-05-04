# 이함수는 두개의 숫자를 inptu 으로 받으면 잓은 수로 큰 수를 나눈 몫과 나머지를 반환하는 함수이다.
# 반환 값은 튜플로 되어 있으면 몫, 나머지 순으로 되어있다.
# 단,0으로 나누는 것은 불가하기 때문에 두수 중 작은 수가 0이라면 화면에 '0은 사용할 수 없습니다' 를 출력하고 종료되어야한다



# def div2 (a, b):
#     if a == 0 or b == 0 :
#         print('0은 사용할 수 없습니다.')
#     elif a < 0 or b < 0 :
#         print('정수를 입력해주세요')
#     elif a > b :
#         print((a//b, a%b))
#     elif b > a :
#         print((b//a, b%a))

# div2(4, 5)

# div2(0, 5)

# div2(-1, 5)

# def div3 (a,b):
#     if a>b :
#         big = b
#         small =a
#     elif b<= a:
#         big = a
#         small=b
#     else:
#         print('정수가 아닙니다')
#     if small == 0:
#         print('0은 사용할 수 없습니다')
#     elif abs(big)<0 or abs(small)<0 :
#         print('정수를 입력해주세요')
#     else:
#         q = big//small
#         r = big%small
#         return (q ,r)
    
# print(div3(5, 4))



# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜보자.
# 끊는 단위는 따로 정하지 않으면 2로 설정해보자.

# def func(string, unit = 2):
#     i = 0
#     while i < len(string):
#         print(string[i:i+unit])
#         i += unit

# print(func('테스트를 위한 문장입니다'))


# def test(*args):
#     print(args)

# test(1,2,4,5,5)

# def test2(**args):
#     print(args)

# test2(a=1, b=2)


# 230.p

# args 는 튜플로 나타낸다

# def add_all(*args):
#     a = 0
#     for i in range(len(args)):
#         a += args[i]
#     return a

# print(add_all(5, 3, 2, 1))

  

# def add_all(*inputs):
#     s=0
#     for i in range(len(inputs)):
#         s +=inputs[i]
#     return s


# print(add_all(5, 3, 2, 1))

# print(add_all([1,2,3,4,5])) #리스트는 에러난다

# def add_all3(*args):
#     s=0
#     for i in args:
#         for j in i:
#             s +=j
#         return s

# print(add_all3(1, 2, 3, 4)) # 2번 돌리면 튜플론 안됨
# print(add_all3([1,2,3,4,5])) #for문 2번 돌리면 리스트로는 가능

# def add_all4(*args):
#     temp=0
#     for i in range(len(args)):
#         if type(args[i]) == list:
#             for j in args[i]:
#                 temp +=j
#         else :
#             temp +=args[i]
#     return temp


# print(add_all4(1,2,3,4))
# print(add_all4([1,2,3,4]))  #저렇게 짜면 리스트, 튜플 둘다 가능


# 239.p 
# 팩토리얼 (Factorial)을 구하시오
# 1부터 시작하여 어떤 범위에 있는 모든 정수를 곱하는것


# def Factorial(a):
#     c =1
#     for i in range(1, a+1):
#         c = c * i
#     return c

# print(Factorial(5))

#재귀적으로 하는 것.
# def fact(n):
#     if n<=1: #n이 1이하이면 종료조건
#         return 1
#     return n*fact(n-1)

# print(fact(5))

# 함수는 사람이름으로 되어 있는 리스트를 받아서 "대기번호x번:사람이름"를 화면에 출력하고(번호표, 사람이름)을
# 원소로 이루어진 리스트를 반환한다.

# people = ['펭수', '뽀로로', '뚝딱이', '텔레토비']
# def func1(line):
#     new_lines = []
#     x = 1
#     for i in line:
#         print("대기번호 %d번 %s" % (x, i)) #%b % 뒤의 정수를 할당 , %s %뒤의 문자를 할당
#         new_lines.append((x, i))
#         x += 1
#     return new_lines

# lines = func1(people)


# enumerate(열거하다)
# 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수
# ist = ['a', 'b', 'c']
# for x in enumerate(ist):
#     print(x)

# people = ['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#     new_lines = []
#     for idx,val in enumerate(line):
#         print('대기번호 %d번 : %s' %(idx,val))
#         new_lines.append((idx+1,val))
#     return new_lines
# lines = func1(people)


# # zip
# 반복가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수.
# 각 원소들을 튜플의 형식으로 묶어줌
# str_list = ['one','two','three','four']
# num_list = [1,2,3,4]


# for i in zip(num_list,str_list):
#     print(i)
# (1, 'one')
# (2, 'two')
# (3, 'three')
# (4, 'four')


# lambda : 한 줄을 실행한 결과 값이 바로 반환값이됨

# func2 = lambda x : x +2

# c = func2(2)

# print(c) ->4

# map 
# 리스트, 튜플, 스트링 등 자료형 각각의 원소에 동일한 함수를 적용
# items = [1,2,3,4,5]
# squared_map = list(map(lambda x : x**2, items))

# print(squared_map)


# 251.p lambda와 map 을 이용하여 items의 요소들을 string(문자)로 바꾸는 것을 짜봅시다.
# items = [1, 24 , 3, 6, 7]

# str_items = list(map(lambda x : str(x), items))

# print(str_items)


#  0~ 9까지 순서대로 가지고 있는 리스트를 만드세요
#1.
# list_1 = [0,1,2,3,4,5,6,7,8,9]
# #2.
# list_2 = []
# for x in range(10):
#     list_2.append(x)
# print(list_2)



# lc_1 = [x for x in range(10)]
# print(lc_1)

# 225.p 
# 1. 구구단 2단을 list comprehension을 이용하여 구현하고 리스트 화면에 출력해보자
# 2. 다음 문장을 분석해보자 
# "코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 마스크를 끼고 손 씻기를 생활화 합시다"
# 라는 문장을 띄어쓰기 별로 분석하려고 한다. 띄어쓰기별로 문장을 나눈 후 각 요소의 길이를 리스트에 저장하라.

# for i in range(2, 3):
#     for j in range(1, 10):
#         print(i ,"x", j, "=", (i*j) )

#1) 구구단 2단
# tables = [2 *x for x in range(1,10)]
# print(tables)

# sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'

# len_sent = [len(s) for s in sentence.split()]
# print(len_sent)

# P.258

# - for 문+if 문
# 10부터 20까지의 숫자들 중에서 짝수만을 담은 리스트를 만들어보자!
# list3 = []
# for x in range(10,21):
#     if x%2==0:
#         list3.append(x)
# print(list3)

# lc_2 = [x for x in range(10, 21) if x%2==0]
# print(lc_2)

# 1부터 10까지의 제곱수중 , 50이하인 수만 리스트에 저장하라
# lc_3 = [x for x in range(1, 11) if x*x<=50]
# print(lc_3)

# #  다음 문장을 분석해보자
# # '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다.마스크를 끼고 손씻기를 생활화 합시다" 라는 문장을
# # 띄어쓰기별로 분석하려한다. 띄어쓰기별로 문장을 나눈 후 각 요소의 길이가 5미만인것을 리스트에 저장

# sentence = '코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다.'
# lc_4 = [s for s in sentence.split() if len(s) <5]
# print(lc_4)

# for+if+else
# 1부터 10까지의 숫자들 중 홀수 이면 어떤 제곱수를, 짝수이면 세제곱수를 담은 리스트를 만들어보자.

# list_4 = []
# for x in range(1,11):
#     if x%2!=0:
#         list_4.append(x**2)
#     else :
#         list_4.append(x**3)
# print(list_4)



# a=[x**2 if x%2==0 else x**3 for x in range(1,11)]
# print(a)


# word1 = 'hello'
# word2 = 'world'

# result = [i+j for i in word1 for j in word2]
# print(result)

# 261.p
# 1. 40 이하의 숫자는 5를 더하고 40초과의 숫자는 41로 바꾸어리스트로 저장하고, 리스트를 출력하라
# b =41
# a =  [x+5 if x<=40 else 41 for x in range(30, 100)]
# print(a)

# 컷트라인이 60점일때 시험이름과 통과여부를 리스트로 담아서 출력하라 이름과 통과여부는 튜플로 묶여있는자료이다

# students = {"보라돌이":61, "뚜비":35, "나나":78,"뽀":88}
# print(students.items())
# result = [(name,True) if score>60 else (name, False)for name,score in students.items()]
# print(result)

#  items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

import numpy as np

# n=1000000
# numpy_arr = np.arange(n)
# python_list = list(range(n))
# print(python_list)

# import time
# start = time.time() #시작시간 저장
# python_list = [x**3+10 for x in python_list]
# print('time:', time.time() - start) #현재시각-시작시간 = 실행시간

# print(time)

# A = [1,2,3,4]

# a = np.array(A, np.int)
# print(type(a))
# print(a)

# -벡터화 
# -배열은 for문을 작성하지 않고 데이터를 일괄처리 하는 것.
# arr = np.array([[1,2,3],[4,5,6])
# print(arr)
# print(arr+ arr)

# 브로드캐스팅
# 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy의 기능.
# import numpy as np

# a = np.array([[ 0.0,  0.0,  0.0],
#               [10.0, 10.0, 10.0],
#               [20.0, 20.0, 20.0],
#               [30.0, 30.0, 30.0]])
# b = np.array([1.0, 2.0, 3.0])

# print(a + b)



import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])
# arr4 = np.array([[1, 2, 3],[4, 5, 6]])


# print(arr+arr4)


# arr_1 = np.array([1,2,3])
# print(arr_1+arr_1)

# print(arr.dtype)
# # dtype
# # 배열에 담긴 원소의 자료형(ndarray는 같은 자료형을 담음.)

# # - size
# #      - 배열에 있는 원소의 전체 갯수

# # arr.size


# # ndim
# # 배열의 차원의 갯수
# print(arr.ndim)

# arr.shape


# 0 차원
# import numpy as np
# a = np.array(10)
# print(a)
# print(a.ndim)

# # 1차원
# a= np.array([1,2,3])
# print(a)
# print(a.ndim)

# # 2차원
# a = np.array([[1,2],[3,4]])
# print(a)
# print(a.ndim)
# print(a.shape)

# 3차원

# a = np.array([[[1,2],[3,4]]])

# print(a)
# print(a.ndim)
# print(a.shape)

# 3차원은 안씀

# range함수를 이용

# arr1 = np.array(range(20))
# print(arr1)


# arr2 = np.arange(20)
# print(arr2)



# print(np.zeros(6)) # [0. 0. 0. 0. 0. 0.]

# print(np.full((4),5)) # [5 5 5 5]

# print(np.empty((2,3),dtype=np.float32))

# print(np.arange(-3, 3)) # [-3 -2 -1  0  1  2]

# print(np.arange(-3, 50, 3)) # [-3  0  3  6  9 12 15 18 21 24 27 30 33 36 39 42 45 48]

# print(np.linspace(0, 1, 6)) #잘개 쪼갠다 [0.  0.2 0.4 0.6 0.8 1. ]


# 배열 결합 함수
# hstack, concatenate(axis=0)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])

# print(np.hstack([a, b]))

# print(np.concatenate((a,b),axis=1))

# a = np. array([1,2,3])
# b = np.array([4,5,6])
# # vstack
# # 배열을 세로로 결합할 때 사용합니다.
# print(np.vstack([a,b]))


# # 두 배열을 위아래로 붙이기

# print(np.column_stack([a,b]))

import random

# print(random.random()) 

# data = [1, 2 ,3 ,4 ,5 ,6 ,7]
# print(np.random.choice(data,3)) #np를 사용하면 여러개를 뽑을 수 있다


# seed
# 난수 초기값 부여 -> 재현 가능성(Reporducibility)
# print(np.random.seed(42))

# print(np.random.rand(1000))
# import numpy as np

# a = int(input("로또 번호를 몇개 생성할까요?"))
# for i in range(a):
#     print("로또번호: ", np.random.choice(range(50), 6))

# import numpy as np

# a = int(input("로또 번호를 몇개 생성할까요?"))
# for i in range(a):
#     lotto_numbers = np.random.choice(range(1, 51), 6, replace=False)
#     sorted_lotto_numbers = np.sort(lotto_numbers)
#     print("로또번호: ", sorted_lotto_numbers)



# import numpy as np
# def make_lotto(count):
#     for i in range(count):
#         lotto_num = [] #로또 번호가 담길 리스트형 변수
#         for j in range(6): #6번 반복
#             lotto_num = np.random.choice(range(1,46),6,replace=False)
#             lotto_num.sort() #값 정렬
#         print('{}.로또번호:{}'.format(i+1,lotto_num))
        
# count = int(input('로또 번호를 몇개 생성할까요?'))
# print(make_lotto(count))