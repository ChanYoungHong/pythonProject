import sys

input = sys.stdin.readline

'''
1. 검사되는 단어마다 2개 이상 같으면 비슷한 단어로 판단하고 cnt += 1을 해준다

'''

# n = int(input())
#
# standard = list(input().rstrip())
#
# print(standard)
#
# store = []
# for i in range(n - 1):
#     word = input().rstrip()
#     store.append(word)
#
# print(store)
# cnt = 0
# check = 0
#
# for j in store:
#
#     if j.count(standard[0])


# n = int(input())
# target = list(input().rstrip())
# # print(target)
# answer = 0
#
# '''
# 2자리 이상 있으면 비슷한 순자로 생각하고 cnt += 1
# '''
# cnt = 0
# for _ in range(n - 1):
#     compare = target[:]
#     word = input()
#     check = 0
#     for w in word:
#         if w in compare:
#             check += 1
#             # print('check : ', check)
#
#     if check >= 3:
#         cnt += 1
# print(cnt)

    # if cnt < 2 and len(compare) < 2:
    #     answer += 1

N = int(input())
target = list(input()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:]
    word = input() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
