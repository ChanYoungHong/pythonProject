
import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    z = int(input().rstrip())

    if z == 0:
        nums.pop()
    else:
        nums.append(z)

print(sum(nums))