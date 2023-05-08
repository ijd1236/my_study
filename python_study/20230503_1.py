# def add_all(*args):
#     a = 0
#     for i in range(len(args)):
#         a += args[i]
#     return [a]


# print(add_all(1, 2, 3, 4,))

import numpy as np

# arr.flatten

# arr = np.array([1.2],[3.4])
# arr.flatten()


# arr.reshape(3,4) #주어진 shanpe의 약수로 이루어진 shape만 가능
# arr = np.arange(12)

# print(arr.reshape(1,12))

# arr = np.arange(20)
# print(arr.reshape(4,5))

# arr_1 = np.arange(4).reshape(-1,2)
# print(arr_1)

# print(arr_1.transpose())
      
# arr = np.arange(30).reshape(3,2,5)
# print(arr.shape)


# a = [5, 23, 2, 1, 5]
# a.sorted




# x = np.arange(6).reshape(-1,3)
# print(x)
# print(x.T)


#p 54 
# 0부터 20까지의 숫자 배열을 만든 다음에 arr1에는 짝수 arr2에는 홀수가들어가는

# arr = np.arange(0, 21)
# arr1 = []
# arr2= []
# for i in arr:
#     if arr[i] %2 ==0:
#         arr1.append(arr[i])
#     else :
#         arr2.append(arr[i])

# Arr = np.arange(0, 21)
# Arr1 = Arr[Arr%2==0]
# Arr2 = Arr[Arr%2!=0]

# print(Arr1)


# arr1d = np.arange(8)

# print(arr1d[:4])

# 브로드 캐스팅

# lst = list(range(6))


# lst[3] = -1
# print(lst) 
# # 리스트에선 하나만 가능 lst[1:3] = -1 이렇게 불가능

# arr1d = np.arange(8)

# arr1d[3:6] = 100

# print(arr1d) #numpy 에서는 여러개도 가능 브로드 캐스팅



# veiw

# arr2d = np.arange(20).reshape(4,-1)
# print(arr2d)
# print(arr2d[0]) #첫번째 행
# print(arr2d[1][2])  #재귀적 접근 / 1행 2열 = 7
# print(arr2d[1,2]) #컴마를 이용하여 쉽게 인덱싱을 할 수 있음.

# print(arr2d[:3][:2]) #이렇게하면 3번째행 2번째행임 = 2번째행
# print(arr2d[:3,:2]) #이렇게 해야 행과 열을 접근함


#  불리안 배열
# arr = np.array([0,1,2,3,4])
# arr[[True,False,True,False,True]]
# print(arr)


# arr2d = np.arange(20).reshape(4,5)

# arr2d[[0,2]] #0행과 2행 #멀티 인덱스는 []하나 더 추가해야함

# arr = np.arange(-3,3).reshape(3,-1)
# print(np.exp(arr)) 

# floor : 소수점 버리기

# print(np.floor(arr))

# 이항 유너버셜 함수

# arr1 = np.arange(8).reshape(2,-1)
# arr2 = np.arange(-40,40,10).reshape(2,-1)
# print(arr1)
# print(arr2)

# print(np.maximum(arr1,arr2)) #같은 원소에서 가장 큰 값을 뽑아냄

# print(np.subtract(arr1,arr2)) #뺄셈

# print(np.multiply(arr1,arr2)) #같은 원소끼리 곱셈

# 통계 메소드
# arr = np.arange(4).reshape(2,2)
# print(arr)
# print(arr.sum())
# print(arr.sum(axis=0)) #열로접근    
# print(arr.sum(axis=1)) #행으로접근
# print(arr.mean())
# print(arr.mean(axis=0))
# print(arr.mean(axis=1))


# where
# x if 조건 else y의 벡터화 버젼
# numpy를 사용하여 배열을 빠르게 처리할 수 있으며, 다차원도 간결하게 표현가능

# xarr = np.array([100,200,300,400])
# yarr = np.array([1,2,3,4])
# cond = np.array([True,False,True,False])

# result = np.where(cond,xarr,yarr)
# print(result)
# True 일땐 xarr Fals 일땐 yarr

# print(np.where(xarr>200,max(xarr),0))

# print(np.where(xarr%3==0,1,0))

# sort()
# np.random.seed(42)
# arr = np.random.randint(1,100,size=10) #1~100까지의 정수중에 10개를 뽑아주세요
# print(arr)
# print(-np.sort(-arr)) #부호를 이용하여 내림차순으로 정렬.

# # array의 sort에서는 내림차순, 오름차순을 선택하는 옵션이 없다.

# lst = [1,32,4,1,20]
# lst.sort(reverse=True)
# print(lst)


# 선형대수 패키지
# 단위행력
# 대각원소 1이고, 나머지는 0인 n차 정방행렬을 말하며, numpy의 eye()함수를 사용하여서 만들 수 있음.

# import numpy as np
# identity = np.eye(4)
# print(identity)

# identity = np.eye(2,3)
# print(identity)

# 대각행렬 
# 대각성분 이외의 모든 성분이 0인 n차 정방행렬
# x = np.arange(9).reshape(3,-1)
# print(x)

# print(np.diag(x))

# print(np.diag(np.diag(x)))

# dot
# 원소간의 곱 (element-wise product)
# 벡터의 내적(행렬의 곱)


# a = np.arange(4).reshape(-1,2)

# print(a*a)
# print(np.multiply(a,a))

# print(np.dot(a,a)) # 행렬의 곱
# a*a
# np.multiply(a,a)


# matmul : matrix multiplication
# a = np.random.randint(-3,3,10).reshape(2,5)
# b = np.random.randint(0,5,15).reshape(5,3)
# a.shape,b.shape

# ab = np.matmul(a,b)
# print(ab.shape,'\n') #\n : 개행
# print(ab)

# np.dot(a,b) dot -> 1차원 벡터 공식문서에서는 2D matmul로 돌아감


import numpy as np
import pandas as pd


# obj = pd.Series([0,1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g','h'],
#                                           dtype='int64')
# print(obj)

# print(obj[[3]])

# print(obj[[1,3,5]]) #multi index 접근방법

# print(obj[1:3])

# print(obj[obj<3]) #boolean indexing


# label location based

# print(obj)
# print(obj.c)
# print(obj['c'])
# print(obj[['e','c']])
# print(obj['a' : 'd'])
# obj['d' : 'e'] = 100
# print(obj) #브로드캐스팅이 잡아채서 변함

# integer location based (iloc)

# obj = pd.Series([0,1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g','h'],
#                                           dtype='int64')

# print(obj.iloc[2])

# print(obj.iloc[[2]])

# print(obj.iloc[1:4])

# location based

# print(obj.loc['a':'c'])

# df = pd.DataFrame(np.arange(24).reshape(4,-1) ,
#                   columns = ['c1','c2','c3','c4','c5','c6'],
#                   index=['r1','r2','r3','r4'])

# print(df)
# print(df['c3'])

# print(df.c3)

# print(df[['c1', 'c3']])

# print(df['r1' : 'r2'])

# print(df['c1':'c2'])
#df['c1':'c2']는 행 인덱스 슬라이싱입니다. 하지만 이것은 행 슬라이싱을 지원하지 않는 DataFrame입니다. 

# print(df[['c1', 'c2']])

# iloc

# print(df.iloc[[0],[3]])
# # df.iloc[[0,1],1:4]
# # df.loc[['r1'],['c4']]
# print(df.loc['r1':'r2', ['c2','c3','c1']])

# 산술 연산자
# s1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
# s2 = pd.Series([10,20,30,40], index=['a', 'b', 'c', 'd'])
# print(s1+s2)

# s1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
# s2 = pd.Series([10,20,30,40], index=['b', 'c', 'd', 'e'])
# print(s1+s2)#SQLdml Outer jonin
# print(s2.add(s1,fill_value=0))


import pandas as pd

# A = np.array([16,12,28,8,18,17,28,24,5,4,12,16,8,4,4,4])
# print(sorted(A))
# print(np.mean(A))
# print(np.median(A))

# unique
# 중복되는 값을 제거하고 유일한 값만 담고 있는 Series를 반환
# obj = pd.Series([2,1,3,3,1,5,np.nan,1,2])
# print(obj)
# print(obj.isnull().sum())
# print(obj.unique())  #시리즈 밖에 안됨



# value_counts
# print(obj.value_counts(normalize=True))

# print(obj.sort_values())


# obj = pd.Series([1,2,3,-1,-2], index=list('가나다라마'))
# print(obj)



frame = pd.DataFrame(np.arange(9).reshape(3,3), index = list('abc'), columns = list('edf'))

# print(frame)

# print(frame.sort_index())



# print(frame.sort_index(axis=1)) #np 와 다르게 pd 에서는 axis = 1 이 열이다 axis = 0 이 행

# print(frame.sort_values(by='e', ascending=False))
# print(frame.sort_values(by=['e','f'],ascending=[False,True]))

# map
# Series의 각각의 element들을 다른 어떤 값을 대체하는 역할.

series = pd.Series([100,200,300])
print(series)

print(series.map({100:'C',200:'B',300:'A'}))

print(series.map('{}달러'.format))

# f = lambda x : np.add(x,3)
# print(series.map(f))


# apply
# map 보다 더 크게 적용할 수 있음
# s = pd.Series([20,21,12], index=['London','New York','Helsinki'])
# print(s)
# def sub_custom_value(x,val):
#     return x-val
# print(s.apply(sub_custom_value,args=(10,)))


# def add_custom_values(x,**kwargs):
#     for month in kwargs:
#         x +=kwargs[month]
#     return x
# print(s.apply(add_custom_values, june = 30 , july=20, august=25))


# def solution(myString):
#     return sorted(ch for ch in myString.split('x') if ch)

# print(solution("a a"))


# frame = pd.DataFrame(np.arange(12).reshape(3,4),
#                      columns = list('abcd'))
# print(frame)



# print(frame.apply(lambda x : x.max()-x.min())) #axis = 0  이 탑제되어잇음

# print(frame.apply(lambda x : x.max()-x.min(),axis=1))

# print(frame.applymap(lambda x : x **2))
# frame = pd.DataFrame(np.arange(16).reshape(4,4),
#                      index = ['r1','r2','r3','r4'],
#                      columns = ['c1','c2','c3','c4'])
# print(frame)

# print(frame.drop('r1'))


# # print(frame.drop('c1')) #KeyError: "['c1'] not found in axis")

# print(frame.drop('c1', axis=1))



# print(frame.drop(columns=['c3', 'c4']))

