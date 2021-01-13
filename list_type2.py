# p.72 리스트 자료형
# 배열(array) - 시퀀스
# 빈 리스트 <-- mutable 변경 가능한 데이터 타입
a = []
b = [1, 2, 3, 'AA', 'BB', ['Life', 'is', 'egg']]
# list() - 리스트 타입으로 캐스팅(casting) <--> 형변환
# 1. 인덱싱(index) - 값을 가리키는
# # index 0 1 2 3 4
# str1 = '안녕하세요'
# print(str1[0])
# print(str1[1])
# print(b[-1])
#
# # 2. 슬라이싱(P.75) : .slice() <--> [시작:끝값:단계]
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6]
# print(a+b)
# print(b*3)

# >>> : 명령 프롬프트 (CLI)
# print(a[0:2])
# print(a[2:])

empty_list = []
for i in range(10):
    # 리스트에 요소(element)를
    empty_list.append(i ** 2)
print(empty_list)

'''
---리스트의 삭제---
1. del          <-- (인덱스) 값 제거
2. .remove()    <-- 값 제거  
3. .pop()       <-- 마지막 원소를 제거, 기존 리스트를 변환
4. .clear()     <-- 완전히 비워내는
'''
# 리스트의 맨 마지막 요소를 돌려주고, 그 요소는 삭제한다.
empty_list.pop()
# .pop(x) : x번째 요소를 돌려주고 그 요소는 삭제한다.
empty_list.pop(2)
# empty_list.remove(1)
# print(empty_list)
# total = 0
# for number in empty_list:
#     total += number
# print('리스트 요소의 합 : ',total)
'''
---------리스트 관련 함수-------
1. sum() : 리스트 내의 합(sum)
2. .sort() : 순차정렬
3. .reversed() : 역순정렬
4. .index() : 인덱스번호
5. .append() : 리스트의 요소를 (리스트 끝) 추가(1)
6. extend() : 여러개의 요소값을 추가(1)
7. .insert(인덱스, 값) : (원하는 인덱스 위치에) 요소를 추가(3)
8. .count() : 요소의 갯수
'''
# del empty_list[9]
# print('-----변경된 리스트의 값-----')
# print(empty_list)

# # 리스트의 수정
# empty_list[0] = '감'
# empty_list[-1] = 100
# print('----------수정된 리스트의 값--------'
# print(empty_list)
# print(empty_list[99])
print('------역순정렬-----')
# print(empty_list[::-1])
empty_list.reverse()
print(empty_list)
# print(empty_list.index(x36))
empty_list.append(99)
print(empty_list)
empty_list.insert(0,109)
print(empty_list)
empty_list.extend(['A', 'B', 'C'])
print(empty_list)
empty_list.clear()
print(empty_list)