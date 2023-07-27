import sys

input = sys.stdin.readline

n = 10

score, total = 0,0

for _ in range(n):
    a = int(input())
    score += a

    if 100 - total >= abs(100 - score):
        total = score

print(total)



# import sys
#
# input = sys.stdin.readline
#
# ans, score = 0,0
#
# for i in range(10):
#     score += int(input())
#
#     if 100 - ans >= abs(100 - score):
#         ans = score
#
# print(ans)