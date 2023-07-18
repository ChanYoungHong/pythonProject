import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum = 0
total = 0
for i in arr:
    sum += i
    total += sum

print(total)
