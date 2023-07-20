import sys

input = sys.stdin.readline

n = int(input())
length_n = len(str(n))

print('length_n : ', length_n)

cnt = 0

for i in range(length_n-1):
    cnt += 9 * 10 ** i * (i+1)

print(cnt + (n - 10**(length_n-1) + 1) * length_n)


