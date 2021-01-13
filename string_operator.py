# p.49 문자열 연산하기
'''
숫자연산자 : +, -, *, /, %, **, //
문자연산자 : + (연결)
'''
# head = 'python'
# tail = 'is fun!'
# print(head+tail)

# 문자열 연산자 : * (지정 횟수 반복)
# a = 'python'
# print('='*50)
# print(a*10)
# print(10*a)

# len() : 문자열의 길이를 구하는 함수
# p.51
# 인덱싱 : 몇번째 문자(열)을 가리키는 것
# python : 갯수 6개
# 012345
# print(len(head))
# print() 줄바꿈, 줄바꿈 x --> end 옵션
# print(head[0], end='')
# print(head[1])
# print(head[2])
# print(head[3])
# print(head[4])
# print(head[5])

# p.53 / 슬라이싱 : 잘라내는것
string_a = "Life is too short, you need Python"
# Python만 출력한다면?
# [시작:]
# [시작:끝(포함x)]
# [시작:끝:단계]

# print(string_a[28:])
print(len(string_a))
print(string_a[19:-7])
# string_b = "LIFE IS TOO SHORT, YOU NEED PYTHON"
# string_c = string_a[0]+string_a[1]+string_a[2]+string_a[3]
# print(string_c)
# print(string_a[0:4])
# upper(), lower()
# print(string_a.upper())
# print(string_b.lower())

msg_text = 'hello python'
print('python' in msg_text)
# Boolean, Bool , 불(부울)
print(4 > 5)
print(10 == '10')
