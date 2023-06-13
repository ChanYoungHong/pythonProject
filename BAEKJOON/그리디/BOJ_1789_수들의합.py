import sys

input = sys.stdin.readline

'''

1. n개의 합이 s일 때 
2. n개 중에서 최대값을 구하여라
3. 200이 될 수 있는 최대의 경우의 수를 구해야하나 ?

'''

s = int(input())

n = 1

while n * (n+1) / 2 <= s:
    n += 1

print(n-1)
