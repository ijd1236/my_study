# li_1 = ["Hello", "World", "Python"]
#li_1의 원소를 사용하여
#  Hello World Python 이라고 출력하세요

# li_1의 원소를 사용하여.
# Help라고 출력하세요.

# li_2 = [1, 2, 3]
#  li_1과 li_2를 사용하여
# ["Hello", "World", "Python", 1, 2, 3]을 출력하세요

# li_1과 li_2를 사용하여
# ["Hello", "World", "Python", 3] 을 출력하세요

# print(li_1[0], li_1[1], li_1[2])
# join(리스트)
# 리스트의 문자열을 합친다.
# " ".join(li_1) # 중간에 "" 를 넣어서 합친다
# print(" ".join(li_1))
# print(li_1[0] + " " + li_1[1] + " " + li_1[2])

# print(li_1[0][0:3] + li_1[2][0])


# print(li_1 + li_2)
# li_1.extend(li_2)
# print(li_1)
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# print(li_1)

"""
eng 변수, kor 변수, math 변수를 만들고
각 변수는 과목의 시험 점수이다.
영어 점수는 80점
국어 점수는 60점
수학 점수는 50점
3과목 점수의 평균을 내고 
평균 점수에 따라 성적을 출력한다.
A : 90 ~ 100
B : 81 ~ 90
C : 71 ~ 80
D : 61 ~ 70
F : 60 이하
"""
""""
scores = []
sores = list()  # 비어있는 리스트 생성
scores.append(int(input("영어 점수:")))
scores.append(int(input("국어 점수:")))
scores.append(int(input("수학 점수:")))

# avg = (scores[0] + scores[1] + scores[2]) / 3
# sum -> 리스트의 모든 요소를 모두 더한다
avg = sum(scores) / 3
if avg >= 91:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg>= 61:
    print("D")
elif avg <= 60:
    print("F")
"""

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 500원
# 2번 물건 1000원 2번 물건 50원 4번물건 120원이다
"""

no_1 = 500
no_2 = 1000
no_3 = 50
no_4 = 120
age = int(input("나이:"))
money = int(input("보유 잔액:"))

print("구매 갯수" + str(money // no_1), "잔돈" +  str(money % no_1))
print("구매 갯수" + str(money // no_2), "잔돈" +  str(money % no_2))
print("구매 갯수" + str(money // no_3), "잔돈" +  str(money % no_3))
print("구매 갯수" + str(money // no_4), "잔돈" +  str(money % no_4))
"""
"""
age = input("나이:")
money = int(input("돈"))
price = 500
print(money // price)
print(money % price)
"""
"""
age = input("나이:")
money = int(input("돈:"))
prices = [1000, 50, 120]
print(money // prices[0], money % prices[0])
print(money // prices[1], money % prices[1])
print(money // prices[2], money % prices[2])
"""

