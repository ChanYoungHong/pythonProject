# array = [3, 5, 1, 2, 4]
# sum = 0
#
# for x in array:
#     sum += x
#
# print(sum)
#
# for i in array:
#     for j in array:
#         temp = i*j
#         print(temp)
#
# a = 1000
# print(a)
#
# a = -7
# print(a)
#
# a = 0
# print(a)
#
# a = 1e9
# print(a)
#
# a = 0.3 + 0.6
# print(a)
#
# a = 5
# b = 3
# print(a ** b)
#
# a = [1,2,3,4,5,6,7,8,9]
# print(a)
#
# print(a[3])
#
# n = 10
# a = [100] * n
# print(a)
#
# a = [4,3,2,1]
#
# a.reverse()
# print(a)
#
# # 특정 인덱스에 데이터 추가
# # 인덱스 2에 3 추
# a.insert(2, 3)
# print(a)
#
# b = [1,2,3,3,3,4,5,6,6,6,6]
# print(b.count(6))
#
# b.remove(1)
# b.remove(2)
# print(b)
#
# c = [1,2,3,4,5,6,7]
# print(c[3])
#
# array = [i for i in range(20) if i % 2 == 1]
# print(array)
#
# array = [i * i for i in range(1, 10)]
# print(array)
#
# a = [1,2,3,4,5,5,5]
# remove_set = {2, 5}
#
# result = [i for i in a if i not in remove_set]
# print(result)

check = [1,1,2,2,2,8]
a = [0,1,2,2,2,7]
b = [2,1,2,1,2,1]

answer = [i for i in range(6)]

# 처음 머리 속에서 나오는 코드 그런데 배열? 리스트를 어떻게 출력해야하는지 몰라서 답변 참고
# for i in range(6):
#     if check[i] == b[i]:
#         answer[i] = 0
#     else:
#         answer[i] = check[i] - b[i]
#
# print(answer)


# 답변을 보고 list를 자바의 scanner처럼 어떻게 받는지 참고 함
# list를 답변으로 어떻게 넣는 지 몰라서 못 품
b = list(map(int, input().split()))

for i in range(6):
    print(check[i] - b[i], end=' ')
