import sys

input = sys.stdin.readline

n = int(input().rstrip())

n_length = len(str(n))
aa = 0
for i in range(n_length-1):
    aa += 9 * 10 ** i * (i+1)

print(aa + (n - 10 ** (n_length-1) + 1) * n_length)
