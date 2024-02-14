import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

check = list(set(nums))
check.sort()
print(*check)