import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sum = 0
result = [0]

for i in nums:
    sum += i
    result.append(sum)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(result[b] - result[a - 1])




