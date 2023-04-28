# function 함수
# 입력 -> 처리 => 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다.

# 내장 함수(built-in)
# 내장함수는 파이썬이 기본적으로 제공해주는 함수
# print(), len(), zip(), int(), float(), str(), list(), range()


# abs(값)
# absolute의 약자
# 입력한 숫자형 데이터의 절대값을 반환한다.
# print(abs(100)) 100
# print(abs(-100)) 100
# print(abs(3.15)) 3.15
# print(abs(-3.15)) 3.15


# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) 15


# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5])) 5


# min(리스트)
# 리스트에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5])) 1


# chr(정수)
# 정수 1개를 입력받고 해당 정수에 해당하는 유니코드 문자를 반환한다.
# print(chr(65)) A


# ord(문자)
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
# print(ord('A')) 65


# round(값)
# round(값, 자릿수)
# 반올림 함수
# print(print(1.1234)) 1
# print(round(1.234, 2)) 1.23
# print(round(1.351)) 1.4

# 함수 정의(define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결과값 return vlaue
"""
def 함수이름(함수입력값):
    함수 기능코드
    return 함수 결과값

"""
# def 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜서 지어야한다.
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안된다.
# 띄어쓰기 하면 안된다
# 키워드 사용하면 안된다.
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋다.

# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")
# print_names()

# def get_name():
#     return "김주영"

# def print_my_name():
#     print(get_name())

# print_my_name()


# a = print_names() #리턴값이 없음
# b = get_name( ) #리턴이 있음

# print(a) None
# print(b) "김주영"

# return 으로 그 함수가 반환할 값을 정함 return이 없을땐 수행만하고 종료함



# parameter
# 함수에 입력하는 값
# 매개변수, argument 혼용 add(a, b) (a, b)가 매개변수
# def add(a, b):
#     return a +b

# def print_add(a, b):
#     print(a + b)




# add() # Error a, b를 입력안해서 
# add(1, 2) # Error 없이 그냥 종료 (출력x)

# result = add(1, 2) # 리턴이 있는 함수
# print(result) #3


# # print_add(1, 2) # 3 -> 리턴값이 없으면 보통 이렇게 입력함
# result = print_add(1, 2)  #리턴이 없는 함수 -> 그래도 3은 출력된다 기존 할당과는 다름
# print(result)  # print_add는 return하지 않았으므로 None 이 출력된다


# print_add("안녕", "하세요") # 안녕하세요 a= 안녕 b = 하세요
# # print_add("안녕", 1) # Erorr
# print_add(b= "하세요", a = "안녕") # 따로 a , b 자리에 들어갈 값을 지정하면 안녕하세요로 순서 변경해서 출력가능

# def swap_number(a, b):
#     temp = a
#     a = b
#     b= temp
#     print(a, b)
#     return a, b
# a = 1
# b = 2
# print("함수 호출전", a, b) # 1 ,2 
# a, b = swap_number(a, b) # 2, 1,,
# print("함수 호출 후", a, b) # 2, 1
# 함수 (swap_number)안에서의 값과 밖에서의 값은 다르다.
# 이름이 같더라도 서로 다른 변수다
# 전체에서 적용되는 변수는 전역변수 , 함수내에서 적용되는 변수는 지역변수 라고 한다.


# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# def mul(a, b):
#     return a * b


# result  = mul(5, 4)
# print(result) # = print(mul(1,2))

# a = 1
# b = 2
# c = 3
# 이걸 a, b, c = 1, 2, 3 으로 가능 튜플, 인덱스 등도 가능 


# 기본 값 매개변수
# default value parameter
# 함수 호출시 n2에 입력된 값이 없으면 기본 값 사용
# def mul(n1, n2=1):
#     return n1 * n2

# mul(1, 2)
# mul(1) 

def test_func(x, test=[]):
    test.append(x)
    print(x, test)

test_func(1) # 1 [1]
test_func(2) # 1 [2, 3]
# 이렇게 리스트를 기본값으로 사용하면 값이 누적된다 그래서 리스트는 기본값으로 사용하기 적절치 않다

# def test_func(x, test=5):
#     test = test
#     print(x, test)         

# test_func(1) # 1, 5
# test_func(2) # 1, 5

# def test_func1(x, test=None):
#     if test == None:
#         test = []
#     test.append(x)
#     print(x, test)

# test_func1(1)
# test_func1(2)  # 이런식으로 하면 누적되지 않는다

# 기본값이 있는 매개변수는
# 기본값이 없는 매개변수보다 뒤에 위치해야함
# def sub(n1, n2=0, n3): # Non-default argument follows default argumentPylance
#     print(n1 - n2 - n3)


# 1~ 10까지 더한다
# *를 사용한 매개변수
# 입력값이 몇개가 될지 정해지지 않았을 때 사용하게 된다.
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱 ,슬라이싱 가능
#     result = 0
#     for i in args:
#         result += i
#     return result


# result1= add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)

# # 일반 매개변수랑 같이 사용 가능하다
# def calc_many(n1, *args):
#     result = n1 
#     for i in args:
#         result += i
#     return n1


# 키워드 매개변수
# **kwargs(keyword arguments)
# 딕셔너리로 사용
# 뒤에 들어오는 값들이 유동적일때 사용
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1, b=2)   # {'a': 1, 'b': 2}
# print_kwargs(name='이름', age=10) # {'name': '이름', 'age': 10}


# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.
# def test_func5():
#     print(1)
#     print(2)
#     return None # -> 함수 종료
#     print(3)
#     print(4)
#     print(5)
    
# # 함수의 반환값은 무조건 한개이다.

# def test_func6(a, b):
#     a + b, a * b
#     return a + b , a * b # = return (a + b, a * b) 의미와 같다

# print(test_func6(1, 2)) # (3, 2)
# res_add, res_mul = test_func6(1, 2)# = res_add, res_mul = (a+b, a*b)
# print(res_add, res_mul) # 3, 2

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수 인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True, 짝수면 False



# def is_odd_number(n):
#     if n % 2 != 0:
#         return True
#     else:
#         return False
    
# def is_odd_number(n):
#     return n % 2 == 1
      
# adf = is_odd_number(5)
# print(adf)
# is_odd_number(5)


# 테두리를 출력하는 함수
# 문자열을 입력받고 print함수를 이용해 테두리와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시
"""
****
hello
****
"""

# def get_bordered_str(message):
#     message = str(message)
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)

# get_bordered_str("hello")
# get_bordered_str(12345) # 그냥 12345는 len함수를 쓸 수 없다 len은 리스트, 문자열만 가능하다.  위에서 str로 숫자열로 문자열을 변환
# def get_bordered_str(message):
#     print(message[0:5])
#     print(message[5:10])
#     print(message[10:15])
          
# get_bordered_str("*****hello*****")

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면 -> km/h 단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : vleocity
# 반환값 : km/h로 변환된 속도


# def convert_velocity(vleocity):
#     return(str(round((vleocity * 3600) / 1000)) + "km/h")


# a = convert_velocity(500)
# print(a)

# 별 찍기 함수
# 정수를함수에 입력하여 호출하면 해당 정수줄의 별을 화면에 출력한다.
# 함수 이름 : print_sters
# 파라미터 : n
# 반환값 : None

"""
출력결과 n ->1
n ->1
*
n ->2
**
n ->3
***
n ->4
****
"""


# def print_sters(n):
#     for i in range(n):
#         print((i + 1) * "*")
        

# def print_sters(n):
#     for i in range(n): # 0 ~ n -1
#         for j in range(i+1): # 0 ~ i
#             print("*", end = "") # end 는 기본적으로 줄바꿈이 들어감
#         print() # 아무것도 안하고 줄바꿈

# def print_sters(n):
#     i = 0
#     while i < n:
#         j = 0
#         while j < i+1:
#             print("*", end="")
#             j += 1
#         print()
#         i += 1
 


# print_sters(3)


# 1~ 10까지 더한다
# *를 사용한 매개변수
# 입력값이 몇개가 될지 정해지지 않았을 때 사용하게 된다.
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱 ,슬라이싱 가능
#     result = 0
#     for i in args:
#         result += i
#     return result




# def print_sters(n):
#     for i in range(n):
#         print((i + 1) * "*")