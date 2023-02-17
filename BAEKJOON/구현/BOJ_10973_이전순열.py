import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

for i in range(n - 1, 0, -1):

    if num[i] < num[i - 1]:

        for j in range(n - 1, 0, -1):

            if num[i - 1] > num[j]:
                num[i - 1], num[j] = num[j], num[i - 1]
                result = num[:i] + sorted(num[i:], reverse = True)
                print(*result)
                sys.exit(0)

print(-1)
