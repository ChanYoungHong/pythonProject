import sys

input = sys.stdin.readline

a, b = input().split()
answer = []

for i in range(len(b) - len(a) + 1):
    cnt = 0

    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    answer.append(cnt)

print(min(answer))
print(answer)

# a, b = len(word1), len(word2)
# cnt = 0
#
# result = []
# for i in range(a):
#     for j in range(b):
#
#         if word1[i] != word2[j]:
#             result.append()
#
# print(result)
