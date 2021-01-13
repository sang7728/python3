# p.102 불 자료형

# 불, 불리언 / bool , boolean

# True, False vs 참, 거짓

# 명시적인 표현
is_true = True
is_false = False
# 비교 연산자 : >, >=, <, <= , ==, !=
# 논리 연산자 : and, or, not
# print(4 > 5)
print(type(is_true))
print(1==1)
# print(1 is 1)
# p.103 자료형의 참과 거짓 (표)
# 불린 값 True  : 실행함
# 불린 값 False : 실행하지 않음
# '' or "" - 공백문자
# [],(),{} - 리스트,튜플,딕셔너리 (=원소나 값이 없는 상태)
# None , 0

#p.104
a = []
print(type(a))
while a:
    print(a)

# 변수=초깃값
# while 조건문(식):
#   수행할 문장(코드)
#   변수의 증감식

# while 4 < 5:
#     print('안녕하세요')

# 멤버쉽 테스트
print("안" in "안녕하세요")
print("안" not in "안녕하세요")