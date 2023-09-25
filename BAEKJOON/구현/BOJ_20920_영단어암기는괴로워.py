import sys

input = sys.stdin.readline

# n, m = map(int, input().split())
#
# wordDict = {}
# # n = int(input())
#
# for i in range(n):
#
#     a = input().rstrip()
#
#     if a not in wordDict:
#         wordDict[a] = 0
#     wordDict[a] += 1
#
# # print(wordDict)
# # wordDict.sort()
#
# # sorted_dict = sorted(wordDict.items())
# sorted_dict = sorted(wordDict.items(), key = lambda item: item[1], reverse = True)
#
# for k,v in sorted_dict:
#
#     # max_key = max(wordDict, key = wordDict.get)
#     #
#     # print('max_key : ', max_key)
#
#     if len(k) >= m:
#         # print('k = ', k)
#         print(k)
#
# # print(sorted_dict)


n,m = map(int, input().split())
d = {}

for _ in range(n):
    name = input().rstrip()

    if len(name) < m:
        continue

    if d.get(name):
        d[name][0] += 1
    else:
        d[name] = [1, len(name), name]

ans = sorted(d.items(), key=lambda x : (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
    print(a[0])