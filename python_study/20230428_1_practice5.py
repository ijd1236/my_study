# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요.
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False

# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "") #문자열 중간에 있는 공백 제거
#     # for i in range(length//2): #회문이라 반만 검사
#     #     if input_string[i] != input_string[length - 1- i]:
#     #         return False
#     #     return True
#     return input_string == input_string[::-1] #리스트뒤집기


# ag = is_palindrome("소주 만병만 주소")
# print(ag)


# reversed("안녕하세요")
# li1 = [1,2,3,4,5]
# li1.reverse()
# print(li1)
# li2 = [1,2,3,4,5]
# reversed(li2) 
# print(li2) #원본은 그대로 두고 값만 출력

# string1 = "안녕하세요"
# string2 = reversed(string1)  #안나옴
# print(string2)  #안나옴 immutable;;
# for i in string2:
#     print(i)
# string3 = "".join(string2)
# print(string3) #거꾸로 출력 





