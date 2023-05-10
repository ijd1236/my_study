import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.datasets import load_boston
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# # boston 데이타셋 로드
# boston = load_boston()

# #boston 데이터셋 DataFrame변환
# bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)

# #boston dataset의 target array는 주택 가격
# #이를 컬럼 PRICE 컬럼으로 DataFrame에 추가함.
# bostonDF['PRICE'] = boston.target
# # print('Boston 데이터셋 크기:', bostonDF.shape)
# # print(bostonDF)

# # CRIM : 지역별 점외 발생률
# # ZN : 25,000 평방피트를 초과하는 거주 지역의 비율
# # NDUS : 비상업 지역 넓이 비율
# # CHAS : 찰스강에 대한 더미 변수(강의 경계에 위차한 경우는 1, 아니면 0)
# # NOX : 일산화질소 농도
# # RM : 거주할 수 있는 방 개수
# # AGE : 1940년 이전에 건축된 소유 주택의 비율
# # DIS : 5개 주요 고용센터까지의 가중거리
# # RAD : 고속도로 접근 용이도
# # TAX : 10,000 달러당 재산세율
# # PTRATIO : 지역의 교사와 학생 수 비율
# # B : 지역의 흑인 거주 비율
# # LSTAT : 하위 계층의 비율
# # MEDV : 본인 소유의 주택가격(중앙값)
# fig,axs = plt.subplots(figsize=(16,8), ncols=4,nrows=2)
# lm_features = ['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
# for i,feature in enumerate(lm_features):
#     row = int(i/4)
#     col = i%4
#     #seaborn의 regplot을 이용해 산점도와 선형 회귀 직성을 함께 표현
#     sns.regplot(x=feature, y='PRICE', data= bostonDF,ax = axs[row][col])




# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# y_target = bostonDF['PRICE']
# X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)

# X_train,X_test,y_train,y_test = train_test_split(X_data,y_target,test_size=0.3,
#                                                  random_state=156)

# #linear Regression OLS(ordinary Least Square(OLS) method)
# #error function을 gradient method로 학습/예측/평가 수행.
# lr = LinearRegression()
# lr.fit(X_train,y_train)
# y_preds = lr.predict(X_test)
# mse = mean_squared_error(y_test, y_preds)  
# rmse = np.sqrt(mse)
# # print('MSE : {0:.3f} , RMSE : {1:.3F}'.format(mse , rmse))
# # print('Variance score : {0:.3f}'.format(r2_score(y_test, y_preds)))

# # print('절편 값:', lr.intercept_)
# # print('회귀 계수 값:',np.round(lr.coef_,1))


# # 회귀 계수를 큰 값 순으로 정렬하기 위해 Series로 생성. index가 컬럼명에 유의
# coeff = pd.Series(data=np.round(lr.coef_, 1), index=X_data.columns )
# coeff.sort_values(ascending=False)
# # K-fold cross validation
# # K 겹 교차 검증(Cross validation)이란 통계학에서 모델을 "평가" 하는 한 가지 방법입니다. 
# # 소위 hold-out validation 이라 불리는 전체 데이터의 일부를 validation set 으로 사용해 모델 성능을 평가하는 것의 문제는 데이터셋의 크기가 작은 경우
# #  테스트셋에 대한 성능 평가의 신뢰성이 떨어지게 된다는 것입니다. 만약 테스트셋을 어떻게 잡느냐에 따라 성능이 다르면, 우연의 효과로 인해 모델 평가 지표에 편향이 생기게 됩니다.

# # 이를 해결하기 위해 K-겹 교차 검증은 모든 데이터가 최소 한 번은 테스트셋으로 쓰이도록 합니다. 
# # 아래의 그림을 보면, 데이터를 5개로 쪼개 매번 테스트셋을 바꿔나가는 것을 볼 수 있습니다.
# #  첫 번째 Iteration에서는 BCDE를 트레이닝 셋으로, A를 테스트셋으로 설정한 후, 성능을 평가합니다. 두 번째 Iteration에서는 ACDE를 트레이닝셋으로,
# #  B를 테스트셋으로하여 성능을 평가합니다. 그러면 총 5개의 성능 평가지표가 생기게 되는데, 보통 이 값들을 평균을 내어 모델의 성능을 평가하게 됩니다. (아래 데이터는 모두 사실은 트레이닝 데이터입니다. Iteration이라는 상황안에서만 테스트셋이 되는 것입니다.)
# #  이 때, 데이터를 몇 개로 쪼갰느냐가 K-겹 교차검증의 K가 됩니다.
# # 출처: https://3months.tistory.com/321 [Deep Play]


# # 우리는 과적합(overfitting)을 방지하는 것이 중요하다.
# # 과적합이란 train에서 성능이 좋고 Test에서 성능이 좋지 않는 것이다.
# # 반대는 과소적합(underfitting)이라고 함.

# from sklearn.model_selection import cross_val_score

# y_target = bostonDF['PRICE']
# X_data = bostonDF.drop(['PRICE'],axis=1,inplace=False)
# lr = LinearRegression()

# # K-Fold Cross validation
# # cross_val_score( )로 5 Fold 셋으로 MSE 를 구한 뒤 이를 기반으로 다시  RMSE 구함. 

# neg_mse_scores = cross_val_score(lr,X_data,y_target,scoring='neg_mean_squared_error',cv=5)
# rmse_scores = np.sqrt(-1*neg_mse_scores)
# avg_rmse = np.mean(rmse_scores)

# #cross_val_score(scoring ='neg_mean_squared_error')로 반환된 값은 모두 음수
# #회귀의 값은 작아지면 좋으니깐 마이너스를 취하면 작으면 작아지는게 좋음
# print('5 folds의 개별 negative MSE scores:',np.round(neg_mse_scores,2))
# print('5 folds의 개별 RMSE scores:', np.round(rmse_scores,2))
# print('5 folds의 평균 scores: {0:.3f}'.format(avg_rmse))

import pandas as pd

train = pd.read_csv('C:/Users/405/Desktop/새 폴더 (2)/train.csv')
test = pd.read_csv('C:/Users/405/Desktop/새 폴더 (2)/test.csv')

# 탐색적 자료 분석(Exploratory Data Analysis(EDA)
# survived : 생존=1, 죽음=0
# pclass : 승객 등급. 1등급=1, 2등급=2, 3등급=3
# sibsp : 함께 탑승한 형제 또는 배우자 수
# parch : 함께 탑승한 부모 또는 자녀 수
# ticket : 티켓 번호
# cabin : 선실 번호
# embarked : 탑승장소 S=Southhampton, C=Cherbourg, Q=Queenstown


# print(train.head()) 
# print(train.tail())

# print(train.shape,test.shape)

# print(train[train['Survived']==1]['Sex'].value_counts())


def bar_chart(feature):
  survived = train[train['Survived'] ==1][feature].value_counts() # 생존자를 카운트
  dead = train[train['Survived'] ==0][feature].value_counts() #사망자를 카운트
  df = pd.DataFrame([survived,dead]) #[생존자,사망자]를 dataFrame
  df.index = ['Survived','Dead'] # index화
  df.plot(kind = 'bar',stacked = True, figsize = (10,5)) #그림을 그림

# bar_chart('Sex') #무슨 이유로 남성분들이 사망을 하셨을까?
# plt.show()

# bar_chart('SibSp') #함께 탑승한 형제 또는 배우자 수에 따라서 생존이 왜 다를까?
# plt.show()

# bar_chart('Parch') #함께 탑승한 부모 또는 자녀 수
# plt.show()


# f,ax = plt.subplots(1,2, figsize=(18,8))
# train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
# #exploed : 각 항목을 파이의 원점에서 튀어나오는 정도를 나타냄
# #autopct : 각 항목의 퍼센트를 표시함.
# #shadow : 그림자를 그릴 것 인지?
# ax[0].set_title('Survived')
# ax[0].set_ylabel('')
# sns.countplot(x=train['Survived'],ax = ax[1])
# ax[1].set_title('Survived')
# plt.show()

# Pclass

# pd.crosstab(train.Pclass, train.Survived, margins=True).style.background_gradient(cmap='summer_r')


# f,ax = plt.subplots(1,2,figsize=(18,8))
# train['Pclass'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'],ax = ax[0])
# ax[0].set_title('Number of Passengers By Pclass')
# ax[0].set_ylabel('Count')
# sns.countplot(x='Pclass',hue='Survived',data = train, ax = ax[1])
# ax[1].set_title('Pclass:Survived vs Dead')
# plt.show()


# sns.pointplot(x='Pclass',y='Survived', hue='Sex',data=train)
# plt.show()


# print('Oldest Passeneger was of :', train['Age'].max(), 'Years')
# print('Youngest Passeneger was of :', train['Age'].min(), 'Years')
# print('Average Age on the ship :', train['Age'].mean(), 'Years')
# print('Median Age on the ship :', train['Age'].median(), 'Years')
# print('Mode Age on the ship :', train['Age'].mode(), 'Years')



# f,ax = plt.subplots(1,2,figsize=(18,8))
# sns.violinplot(x='Pclass',y ='Age',hue='Survived',data = train, split = True,ax = ax[0])
# ax[0].set_title('Pclass and Age vs Survived')
# ax[0].set_yticks(range(0,110,10))
# sns.violinplot(x='Sex',y='Age', hue='Survived',data = train, split=True, ax=ax[1])
# ax[1].set_title('Sex and Age vs Survived')
# ax[1].set_yticks(range(0,110,10))
# plt.show()


# train['Name'].str

# print(train['Name'].str.extract('([A-Za-z]+)\.', expand=False))
#[A-Za-z]+)\. : 정규표현식(regular expression)
# -> 규칙 : 대문자나 소문자로 시작하다가 .으로 끝나면 추출해주세요.



train_test_data = [train,test]
#Name에 따라서 뭐가 다른가?  -> 전에 각각 해당하는 value를 count를 함.
for dataset in train_test_data:
    dataset['Title'] = train['Name'].str.extract('([A-Za-z]+)\.', expand=False)
#extract('([A-Za-z]+)\. ->정규표현식
# A-Z와 a-Z를 찾아서 어느지점에서 끝내는가? .을 기준으로 해서 자르라는 이야기 그 다음에 count

# print(train['Title'].value_counts() )

s2 = pd.Series(['a_b_c','c_d_e', np.nan,'f_g_h'], dtype='string')
# # print(s2)
# s2.str.split('_')
# print(s2)


# print(s2.str.split('_',expand=True)) # 데이터프레임 형식으로 확장되었음.
# print(s2.str.split('_',expand=False)) # 데이터프레임 형식으로 확장되었음.

# 원본 Series에 StringDtype이 있으면 출력 열도 모두 StringDtype이 됨.
# n에 원하는 갯수를 입력하여 분할하고자 하는 수를 제한할 수도 있다.

# print(s2.str.split('_',expand=True,n=1)) # 데이터프레임 형식으로 확장되었음.

# print(s2.str.split('_',expand=True,n=2)) # 데이터프레임 형식으로 확장되었음.


# one-hot encoding

#극단적으로 나눔.
# title_mapping = {'Mr':0, "Miss":1, 'Mrs':2,'Master':3,
#                  'Dr':3,'Rev':3,'Col':3,'Major':3,'Mlle':3,'Ms':3,'Sir':3,'Don':3,'Countess':3,
#                  'Capt':3,'Lady':3,'Jonkheer':3,'Mme':3}
# for dataset in train_test_data:
#     dataset['Title'] = dataset['Title'].map(title_mapping) #모든 피쳐에 적용해주세요.

# bar_chart('Title')
# plt.show()




# sex_mapping = {'male':0,'female':1}
# for dataset in train_test_data:
#     dataset['Sex'] = dataset['Sex'].map(sex_mapping)
# #method : sklearn.preprocessing import OneHotEncoder, pandas의 get_dummies

# bar_chart('Sex')
# plt.show()

# # 결측치 처리

#missing Age를 각 Title에 대한 연령의 중간값으로 채움(Mr,Mrs,Miss,others) inplace 는 채울꺼냐?
train['Age'].fillna(train.groupby('Title')['Age'].transform('median'),inplace=True)
#train에 결측치 처리를 하였다면, test에도 똑같이 처리를 해야됨.
test['Age'].fillna(test.groupby('Title')['Age'].transform('median'),inplace=True)


# print(train['Age'].isna().sum()) #결측치 처리 하고 꼭 다시 확인할 것.


# print(train[['Title','Age']].groupby(['Title'], as_index = False).mean())


# 가설 2) 사망자의 나이가 어떻게 될까? +생존자

import matplotlib.pyplot as plt
import seaborn as sns

#변수의 분포를 시각화하거나, 여러 변수들 사이의 상관관계를 여러개의 그래프로 쪼개서 표현할때 유용함
# FeactGrid는 Colum,row, hue를 통한 의미구분을 통해 총 3차원까지 구현이 가능함.
#aspect : subplot의 세로 대비 가로의 비율.
# facet = sns.FacetGrid(train, hue ='Survived', aspect=4)
# facet.map(sns.kdeplot,'Age',shade = True) # kde : 이차원 밀집도 그래프
# facet.set(xlim=(0,train['Age'].max()))
# facet.add_legend()
# sns.axes_style('dark')

# plt.show()
#20-30대에 사망률 > 생존률이 높다 왜 그럴까?
# facet = sns.FacetGrid(train, hue ='Survived', aspect=4)
# facet.map(sns.kdeplot,'Age',shade = True) # kde : 이차원 밀집도 그래프
# facet.set(xlim=(0,train['Age'].max()))
# facet.add_legend()
# sns.axes_style('dark')

# plt.xlim(20, 30)

# plt.show()
# 20 ~ 30까지 나이로 자름

# 0~80세까지 들어있음. 너무 많다. Pandas ->Binning 기술을 씀 (연속형 변수를 특정한 구간으로 잘라서 범주형으로 만들어주는 기술)

# 잇달아 일어나는 형태의 데이터는 많은 정보를 주지 못하므로 이럴땐 각각 하나의 카테고리에 나이를 담아 정보를 보다 명확하게 확인할 수 있는 방법

# for dataset in train_test_data:
#     dataset.loc[dataset['Age']<=16, 'Age']=0,
#     dataset.loc[ (dataset['Age'] >16) and (dataset['Age']<=26),'Age']=1



# for dataset in train_test_data: 
#   dataset.loc[ dataset['Age'] <= 16, 'Age'] = 0 
#   dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age'] = 1 
#   dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age'] = 2 
#   dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age'] = 3 
#   dataset.loc[ dataset['Age'] > 64, 'Age'] = 4 
#   dataset['Age'] = dataset['Age'].map( { 0: 'Child', 1: 'Young', 2: 'Middle', 3: 'Prime', 4: 'Old'} ).astype(str)

# bar_chart('Age')
# plt.show()

# FamilySize
# 함께 동승한 부모님과 아이들의 수와 형제와 배우자의 수
# 혼자 탄거랑 가족들이랑 탄거랑 어떻게 다를까
# SibSp+Parch

# train['FamilySize'] = train['SibSp']+train['Parch']+1
# test['FamilySize'] = test['SibSp']+test['Parch']+1
# #솔로일 가능성이 있기 때문에 1을 더해줌. 왜냐하면 파이썬은 0부터 숫자를 세기 때문에
# facet = sns.FacetGrid(train, hue ='Survived', aspect=4)
# facet.map(sns.kdeplot,'FamilySize',shade = True) # kde : 이차원 밀집도 그래프
# facet.set(xlim=(0,train['FamilySize'].max()))
# facet.add_legend()

# plt.show()


# 혼자일 경우는 사망률, 생존률이 높음.

X_train = train.drop(['Survived', "PassengerId"],axis=1)
y_train = train['Survived']
X_test = test.drop('PassengerId', axis=1).copy()


X_test['Fare'].fillna(0,inplace=True)

# 원핫인코딩이 힘들어서 우선 포기
X_train.drop('Name',axis=1, inplace=True)
X_test.drop('Name',axis=1, inplace=True)

X_train.drop('Ticket',axis=1, inplace=True)
X_test.drop('Ticket',axis=1, inplace=True)

X_train.drop('Cabin',axis=1, inplace=True)
X_test.drop('Cabin',axis=1, inplace=True)

X_train.drop('Age',axis=1, inplace=True)
X_test.drop('Age',axis=1, inplace=True)

X_train.drop('Title',axis=1, inplace=True)
X_test.drop('Title',axis=1, inplace=True)

X_train.drop('Embarked',axis=1, inplace=True)
X_test.drop('Embarked',axis=1, inplace=True)

X_train.drop('Sex',axis=1, inplace=True)
X_test.drop('Sex',axis=1, inplace=True)

from sklearn.linear_model import LinearRegression
#데이터가 정렬되어 있을 경우도 있기 때문에 데이터를 shuffle 해줌.
from sklearn.utils import shuffle

lig_reg = LinearRegression() #선형회귀 
lig_reg.fit(X_train,y_train)

lig_reg.score(X_train,y_train)


y_pred = lig_reg.predict(X_test)

df1 = pd.DataFrame(y_pred)
# print(df1)


# 당뇨병 예측 하기.



import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
# age : 나이
# sex : 성별
# bmi : 체질량지수
# bp : 평균 혈압
# s1 : 혈중 총콜레스테롤
# s2 : 저밀도 지질단백질
# s3 : 고밀도 지질단백질
# s4 : 총 콜레스테롤 수치
# s5 : 혈중 트리글리세라이드 수치
# s6 : 혈당 수치
diabetes = load_diabetes()
# print(diabetes.data.shape, diabetes.target.shape)
# print(type(diabetes))
# print(diabetes.DESCR)
# plt.scatter(diabetes.data[:,2], diabetes.target)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

df = pd.DataFrame(diabetes.data, columns = diabetes['feature_names'])
df['target'] = diabetes.target
# print(df.head())

# print(df.describe())


# print(df.info())



# print(df.isna().sum()) #결측치

# sns.pairplot(df[["target", "bmi", "bp", "s1"]])
# plt.show()


# df_corr = df.corr()
# print(df_corr)

# cor_order = df_corr.loc[:'s6', 'target'].abs().sort_values(ascending=False)

# print(cor_order)



# # 상관계수가(-1 ~ 1까지 0이면 관계가 없음) 0.5를 넘은 bmi와 s5를 대상으로 산점도와 회귀선을 그려보자.

# names = ['target','bmi','s5']
# diabetes_df = df.loc[:,names]

# names = ['target','bmi','s5']
# diabetes_df = df.loc[:,names]

# plt.figure(figsize=(16,6))
# for i,name in enumerate(names[1:]):
#     ax = plt.subplot(1,2,i+1)
#     sns.regplot(x=name, y=names[0], data = diabetes_df,ax=ax)
# plt.show()


# from sklearn.model_selection import train_test_split

# x_data=diabetes_df.loc[:, ['bmi', 's5']]
# y_data=diabetes_df.loc[:, 'target']

# X_train, X_test, y_train, y_test=train_test_split(x_data, y_data, test_size=0.2, random_state=1)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)


# from sklearn.linear_model import LinearRegression

# lr = LinearRegression()
# lr.fit(X_train, y_train)
# lr.score(X_train,y_train)

# print(np.round(lr.coef_, 2))
# print(np.round(lr.intercept_, 2))

# pred = lr.predict(X_test)

# # bmi prediction

# plt.figure(figsize=(10, 6))
# plt.scatter(X_test['bmi'], y_test, label='test')  
# plt.scatter(X_test['bmi'], pred, c='r', label='predict')  
# plt.legend() 
# plt.show()

# # s5 prediction

# plt.figure(figsize=(10, 6))
# plt.scatter(X_test['s5'], y_test, label='test')  
# plt.scatter(X_test['s5'], pred, c='r', label='predict')  
# plt.legend() 
# plt.show()


# from sklearn.metrics import mean_squared_error

# test_pred = lr.predict(X_test)
# train_pred = lr.predict(X_train)

# train_mse = mean_squared_error(y_train, train_pred) 
# test_mse = mean_squared_error(y_test, test_pred)

# print("train data set RMSE :", round(train_mse**0.5, 3))
# print("test data set RMSE :", round(test_mse**0.5, 3))





# 공공 자전거 수요 예측(Bike Sharing Demand)
# https://www.kaggle.com/c/bike-sharing-demand/overview
# 데이터 소개

# 날짜 및 시간, 기온, 습도, 풍속 등의 정보를 정보를
# 기반으로 1시간 간격으로 자전거 대여 횟수를 기록한 데이터.

# 기록 날짜는 2011년 1월 ~ 2012년 12월까지
# 데이터에 자세한 정보는 소개된 캐글 사이트에서 확인 가능.

import calendar
import numpy as np
import pandas as pd
#from pandas.core.frame import DataFrame
#from pandas.core.series import Series #이렇게 불러도 됨.
import seaborn as sns # 통계적 plot
from scipy import stats #통계
import missingno as msno #결측치 보는 plot
from datetime import datetime #day
import matplotlib.pyplot as plt
import warnings #에러는 아닌데 주희하는게 뜨는것을 방지.
warnings.filterwarnings('ignore')


df_train = pd.read_csv('C:/Users/405/Desktop/bike-sharing-demand/train.csv')
df_test = pd.read_csv('C:/Users/405/Desktop/bike-sharing-demand/test.csv')
sampleSubmission = pd.read_csv('C:/Users/405/Desktop/bike-sharing-demand/sampleSubmission.csv')



# print(df_train.shape, df_test.shape)

# print(df_train.describe())

# print(df_train.info())

# print(df_train['datetime'])

df_train['date'] = df_train.datetime.apply(lambda x :x.split()[0])
df_train['hour'] = df_train.datetime.apply(lambda x :x.split()[1].split(':')[0])
df_train["weekday"] = df_train.date.apply(lambda dateString : calendar.day_name[
    datetime.strptime(dateString,"%Y-%m-%d").weekday()])
df_train["month"] = df_train.date.apply(lambda dateString : calendar.month_name[
    datetime.strptime(dateString,"%Y-%m-%d").month])
df_train["season"] = df_train.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })
df_train["weather"] = df_train.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })

print(df_train.info())

categoryVariablesList = ['hour','weekday','month','season','weather','holiday','workingday']
for var in categoryVariablesList:
    df_train[var] = df_train[var].astype('category')
# print( df_train.info())


# 결측치 확인.

df_train.isna().sum()
#df_train.isnull().sum()

import missingno as msno #결측치 보는 plot
msno.matrix(df_train,figsize=(12,5)) #결측치가 있다면 하얀색 줄이 그어짐.




df_train_1 = df_train.copy() #훼손 방지
df_test_1 = df_test.copy()

df_train_1['datetime'] = pd.to_datetime(df_train_1['datetime'])
print(type(df_train_1))

#dataFrame 가능한 것.
df_train_1['year'] = df_train_1['datetime'].dt.year
df_train_1['month'] = df_train_1['datetime'].dt.month
df_train_1['day'] = df_train_1['datetime'].dt.day
df_train_1['hour'] = df_train_1['datetime'].dt.hour
df_train_1['minute'] = df_train_1['datetime'].dt.minute
df_train_1['second'] = df_train_1['datetime'].dt.second
#요일 데이터 - 일요일은 0
df_train_1['dayofweek'] = df_train_1['datetime'].dt.dayofweek