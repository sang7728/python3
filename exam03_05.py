# p.148
stu_score = [70, 60, 55, 75, 95, 80, 80, 85, 100]
stu_num = 0
total = 0
for score in stu_score:
    stu_num += 1
    total += score
    print(f'{stu_num}번째 학생의 성적 : {score}')
print(f'총점 : {total}')
average = total / 10
print(f'평균 : {average}')
'''
num_a = 10
str_b = 'test'
bool_c = True
bool_d = False

list_e = []
list_f = [1, 3, 5, 7, 9]
list_g = ['A']


dict
set
'''

# p.72
# '나' 또는 "나"로 감싸여져 있으면 --> 문자열
# 인덱싱, 슬라이싱 <---> 리스트도 비슷~!

# empty = []
# odd = [1, 3, 5, 7, 9]
# even = [2, 4, 6, 8, 10]
# list_in_list = [1, 2, ['Life', 'is', 'egg']]
# print(odd+even)

print('='*50)

# Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음의 코드를 리스트 내포(list comprehensive)를 이용해 표현해보자

numbers = [1, 2, 3, 4, 5]

result = []
for num in numbers:
    if num % 2 == 1:
        result.append(num*2)
print(result)
