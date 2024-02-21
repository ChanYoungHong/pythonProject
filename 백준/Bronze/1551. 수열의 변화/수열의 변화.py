import sys

input = sys.stdin.readline


n,k = map(int, input().split())
list = list(map(int, input().split(',')))

for _ in range(k):
    for i in range(n -1):
        list[i] = list[i+1] - list[i]
        
print(','.join(map(str, list[:n-k])))