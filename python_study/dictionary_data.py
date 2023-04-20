# dictionary(딕셔너리) 자료형
#key-vlaue 형태
# key: value
# person = {"이름": "이름", "나이": 18, "점수": { 
#     "영어": 80,
#     "국어": 90,
#     "수학": 100}}
# print(person["나이"])
# print(person["점수"]["영어"])


# dict_1 = {1: 'a'}
# # dict_1['b'] = 2 # 'b' : key-value 쌍 추가
# dict_1[1] = 'c'
# del dict_1[1] # key 가 1인 리스트 삭제
# print(dict_1)


dict_2 = {1: 'a', 2:'b', 3: 'c'}
# # Keys(_)
# # 딕셔너리에서 key 값만 리스트 형태로 가져온다
# dict_keys=dict_2.keys()
# print(dict_keys)
# # values()
# # 딕셔너리에서 value 값만 리스트 형태로 돌려준다.
# dict_values = dict_2.values()
# print(dict_values)
# # items()
# # 딕셔너리에서 key_value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
# dict_items = dict_2.items()
# print(dict_items)

# get()
# key에 대응되는 value를 돌려준다.
# key값이 존재하지않으면 None(아무것도 없다)을 돌려준다.
# dict_2["나이"]
# print(dict_2.get("나이"))
# print(dict_2.get("나이", "나이 불명")) #앞에 넣어준 값이 없으면 뒤에 넣어준 값으로 출력

# # clear()
# 딕셔너리 안의 모든 요소를 지운다
dict_2.clear()
print(dict_2)
