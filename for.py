# p.138 for 문
'''
for 변수 in 리스트(튜플, 문자열):
    수행할 코드1
    수행할 코드2
    ...계속...
'''
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)
# list()
# print(test_list, type(test_list))
# for문을 이용해서 1~10까지 숫자를 출력해봅니다
# for i in range(10):
#     i += 1
#     print(i)
gugudan_sum = 0
for i in range(1,10):
    print(f'2 x {i} = {2*i}')
    gugudan_sum += 2*i
print('2단의 합 : ',gugudan_sum)
