# import sys
#
# input = sys.stdin.readline
# '''
# 1. 각 알파벳의 개수를 temp에 저장
# 2. count() 함수로 for문 돌려서 찾아내기
# 3.
#
# '''
# word = input().rstrip()
# word = word.upper()
#
# print(word)
# temp = {}
#
# for i in word:
#
#     if i not in temp:
#         temp[i] = 0
#     temp[i] += 1
#
# print(temp)
# big = 0
#
# # # hi = []
# # # print('test : ', max(temp))
# # # hi.append(max(temp))
# # # print(hi)
# # # print(len(hi))
# #
# # test = max(temp, key=temp.get)
# #
# # print(test)
#
# # tmp = 0
# # for a,b in temp.items():
# #
# #     if b > tmp:
# #         tmp = b
# #         print(tmp)
#
#

word = input().rstrip().upper()
array = list(set(word))

cnt_array = []
for i in array:
    cnt_array.append(word.count(i))


if cnt_array.count(max(cnt_array)) > 1:
    print('?')
else:
    max_index = cnt_array.index(max(cnt_array))
    print(array[max_index])