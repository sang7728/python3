# p.130 while 문
# 제어문 > 반복문 > while, for (다른 언어 do while)
'''
변수 = 초기값
while 조건문(식):
    반복 수행할 문장1
    반복 수행할 문장2
    .......문장.....
    증감식
'''

# 변수 --> 의미있는 단어 (키워드x) 조합
# i = 1
# num_sum = 0
# while i <= 100:
#     num_sum += i
#     print(i)
#     i += 1
# print("1~10까지 숫자의 총합 : ",num_sum)

# 구구단
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
..계속...
2 x 9 = 18
'''
# Q. 구구단의 합을 구하여, 반복문 끝나면 출력해보세요!
j = 1
dan = int(input('몇단을 알고 싶으신가요?'))
dan_sum = 0
while j<10:
    dan_sum += dan*j
    print(f'{dan} x {j} = {dan*j}')
    j += 1
print(f'{dan}의 합 : {dan_sum:,}')







