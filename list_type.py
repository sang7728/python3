# p.144 리스트 내포(list comprehensive)
# (java)배열 <---> (python)리스트

a = [1, 2, 3, 4]
# print(a*3)
# 리스트 타입, 원소가 x , 빈(empty)
# result = [num*3 for num in a]
# print(type(a))
# print(len(a))
# for num in a:
#     result.append(num*3)
# print('result : ',result)

# 랜덤모듈(난수발생) - 파이참, 가상환경(venv)

import random
random_list = []
# .append() : 배열에 값을 추가하는 명령어
# 반복문을 다룰줄 안다 : while, for
for i in range(10):
    random_list.append(random.randint(1,10))

print(random_list)