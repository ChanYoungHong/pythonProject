import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

sum = 0
result = [0]
for i in nums:
    sum += i
    result.append(sum)
    print(sum)

for _ in range(m):
    a, b = map(int, input().split())
    print(result[b] - result[a-1])