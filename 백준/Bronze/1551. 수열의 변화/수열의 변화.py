import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num_list = list(map(int, input().split(',')))

for _ in range(k):
    for i in range(n - 1):
        num_list[i] = num_list[i + 1] - num_list[i]

print(','.join(map(str, num_list[:n - k])))