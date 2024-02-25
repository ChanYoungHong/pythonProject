import sys

input = sys.stdin.readline

'''
1 2 3 4 5 6 7
1 2 2 3 3 3 4 4 4 4 5 

'''
a,b = map(int, input().split())

nums = [0]
for i in range(1, b+1):
    for j in range(i):
        nums.append(i)

total = 0
for i in range(a, b+1):
    total += nums[i]

print(total)