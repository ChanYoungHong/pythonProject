import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ans = 0
per = permutations(nums)

for i in per:

    total = 0
    for j in range(len(i) - 1):
        total += abs(i[j] - i[j + 1])

    if total > ans:
        ans = total


print(ans)