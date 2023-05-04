
import numpy as np
import pandas as pd

# 데이터 병합
# concat

# s1 = pd.Series([100,200], index=['c', 'd'])
# s2 = pd.Series([300,300,300], index=['c', 'd','e'])
# s3 = pd.Series([500,600], index=['f', 'g'])
# print(s1,s2,s3, sep='\n\n')

# print(pd.concat([s1,s2,s3]))

# print(pd.concat([s1,s2],axis=1)) #SQL의 outer join(합집합) 으로 들어감

# Merge
# Key를 이용해 데이터의 row를 기준으로 연결시켜 합침(SQL의 join과 유사)



# data1 = pd.DataFrame({'id':['01','02','03','04','05','06'],
#                       'col1':np.random.randint(0,50,6),
#                       'col2':np.random.randint(1000,2000,6)
#                       })
# print(data1)



# data2 = pd.DataFrame({'id':['04','05','06','07'],
#                       'col1':np.random.randint(1000,5000,4)})
# print(data2)



# #inner 
# print(pd.merge(data1,data2,on='id')) #on은 기준

# #how : 어떤 방식으로 병합할 것 인가?{inner,outer,left,right}
# print(pd.merge(data1,data2,on='id',how='left')) #on은 기준


# #outuer join(합집합)
# print(pd.merge(data1,data2,on='id',how='outer')) #on은 기준

# missing data
# dropna : 결측치가 있는 것을 삭제.

# obj = pd.Series(['apple','mango',np.nan,None,'peach',1])

# print(obj)

# print(obj.dropna())  #None가 삭제됨


# frame = pd.DataFrame([[np.nan,np.nan,np.nan,np.nan],
#                       [10,5,40,6],
#                       [5,2,30,8],
#                       [15,3,10,np.nan]
#                       ],
#                      columns = ['x1','x2','x3','x4'])
# print(frame)

# print(frame.dropna()) #Nan 이 있는 모든 행 제거
# print(frame.dropna(how='all')) #행의 모든 값이 Nan 일 경우 제거 

# frame.fillna(0) #method : ffill, bfill,backfill,'pad',None
# frame.fillna({'x1':10,'x3':3})
# frame.isna().sum()

# 중복제거
# 1. duplicated() : 각 row가 중복인지 (True) 인지 False 인지 알려주는 불리언 Series 변환
# 2. drop_duplicates() : duplicated를 적용한 결과가 False 인 것들만 모아서 detaframe 반환.

# data = pd.DataFrame({'id':['0001','0002','0003','0001'],
#                      'name':['a','b','c','a']})
# print(data)

# print(data.duplicated()) #중복 체크

# print(data.drop_duplicates()) #중복 삭제

# # cut


ages = [20,35,67,39,59,44,56,77,28,80,32,46,52,19,33,5,15,50,29,21,33,48,85,80,31,10]
bins = [0,20,40,60,100]

cuts = pd.cut(ages,bins)
# print(cuts)

# print(cuts.categories) #cut 메소드의 결과는 Categorical이라는 특수 객체에 존재.

# print(cuts.codes)


#구간을 균등한 길이로 나눔.
# print(pd.cut(ages,4,precision=1).value_counts())

# #구간을 균등한 길이로 나눔.
# print(pd.qcut(ages,4))

# get)dummies

import pandas as pd

kbo = pd.read_csv('https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/kbo.csv')
kbo

# print(kbo)

# print(kbo.shape)

# print(kbo.columns)

# print(kbo['팀'].unique())

# print(kbo.info())

# print(kbo.isna().sum())
#kbo.isnul().sum()


# gruopby를 하여 group으로 묶인 Groupby 객체를 반환
# 이 객체는 그룹 연산을 위해 피요한 모든 정보를 가지고 있음.
# print(kbo.groupby('팀'))

# print(kbo.groupby('팀').count())

# print(kbo.groupby(['연도','팀']).sum())

# print(kbo.groupby('팀')['승률'].max())

# print(kbo.groupby(['연도','팀'])['승률','순위'].max())

# grouped = kbo.groupby('팀')

# for name,group in grouped:
#     print(name)
#     print(group)

#     print('-'*50)






import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/paskhaver/pandas-in-action/master/chapter_01_introducing_pandas/movies.csv', index_col='Title')
# print(df)

# 객체는 데이터를 저장하는 컨테이너라고 생각하면 좋음.
# 서로 다른 객체는 서로 다른 유형의 데이터에 최적화되어 있으며 서로 다른 방식으로 상호작용함.
# 판다스는 한 가지 유형의 객체(DataFrame)를 사용하여 다중 열의 데이터셋을 저장하고 다른 유형의 객체(Series)를 사용하여 단일 열 데이터셋에 저장. DataFrame은 엑셀의 다중 열 테이블과 유사.
# Rank(순위), Title(제목), Stuido(제작사), Gross(총수익), Year(개봉연도)
# 두 번째 행에는 첫 번째 레코드 또는 첫 번째 영화의 데이터가 나열됨.

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.size)
# print(df.dtypes) #dtype 보다는 info 가 더 좋음
# print(df.info())

#  500번 째 영화를 꺼내보세요
# print(df.iloc[499])
# print(df.loc['Forrest Gump'])

# print(df.sort_values(by="Year", ascending=False).head())
# print(df.sort_values(by=['Studio','Year']).head())
# print(df.sort_index().head())

# 하나 이상의 기준으로 열을 필터링

# print(df['Studio']=='Universal')
# print(df[df['Studio']=='Universal'])

# 만약 index)col을 옵션을 선택안했을경우

# import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/paskhaver/pandas-in-action/master/chapter_01_introducing_pandas/movies.csv')
# df

# df[df['Title'] == 'Forrest Gump']


# 2015년에 개봉한 영화를 필터링할 수 있음 (Universal)
# print(df.loc[(df['Year'] == 2015) & (df['Studio'] == 'Universal')])
# print(df[(df['Studio'] =='Universal') & (df['Year'] ==2015)])

# 1983년에서 1986 사이에 개봉한 영화
mid_80s = df["Year"].between(1983, 1986)
# print(df[mid_80s])
# print(df[(df['Year']>1983) & (df['Year'] <1986)])

# 인덱스에서 영화 제목을 소문자로 바꾸고 제목에 'dark'라는 단어가 있는 모든 영화를 찾는 예제
has_dark_in_title = df.index.str.lower().str.contains('dark')
# print(df[has_dark_in_title])

df['Gross'].str.replace(
    "$","", regex = False
).str.replace(",","", regex=False)

# 참고 : 정규표현식(https://hamait.tistory.com/342)
df['Gross'] = (
    df['Gross']
    .str.replace("$","", regex = False)
    .str.replace(",","", regex=False)
    .astype(float)
)
# print(df['Gross'].mean())

studios = df.groupby('Studio')

print(studios['Gross'].count().sort_values(ascending=False).head())
studios['Gross'].sum().head()
# print(studios['Gross'].sum().sort_values(acending=False).head())






import matplotlib.pyplot as plt

# data = [10,40,20,60,70]
# plt.plot(data)
# plt.show()
import numpy as np

# x = np.arange(10)
# y = x+10

# plt.plot(x,y)
# plt.show()

# plt.xlim([0,10])
# plt.ylim([0,20])

# plt.plot(x,y)
# plt.show()

# x = np.arange(-np.pi,np.pi,0.02)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x,y1,label='sin', color=(0.1,0.3,0.5))
# plt.plot(x,y2,label='cos',color= '#00FF00')
# plt.legend()
# plt.show()




# plt.plot([1,2,3,4],[2,3,5,10],'bo--') #blue+ o 마크 + -- 이것으로 이어주세요
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.show()





# Face color

# x = np.arange(10)
# y1 = x
# y2 = x**2 -x

# fig,axs = plt.subplots(2,1) #2행 1열로 그리겠습니다.
# fig.set_facecolor('#c79fef') #뒤의 배경

# axs[0].plot(x,y1) #첫번째 행
# axs[1].plot(x,y2) #두번째 행

# axs[0].set_facecolor('pink') #첫번째 행의 배경
# axs[1].set_facecolor('skyblue') #두번째 행의 배경

# plt.show()

# Line plot
# x = np.arange(-5,5,0.5)
# y1 = x
# y2 = x**2
# y3 = np.sin(x)
# y4 = np.cos(x)

# plt.plot(x,y1)
# plt.plot(x,y2, marker='D')
# plt.plot(x,y3, color='r')
# plt.plot(x,y4, linestyle = 'dashed')
# plt.show()

# bar plot
# data = {'사과':21, '바나나':15, '배':5,'키위':20}
# names = list(data.keys())
# values = list(data.values())

# fig,ax = plt.subplots()
# ax.bar(names,values)
# plt.show()

# hist

# data = np.random.rand(10000)
# fix,ax = plt.subplots()
# ax.hist(data,bins=100,facecolor='r')
# plt.show()

# 2D Scatter plot

n=50

x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x,y)
plt.show()

