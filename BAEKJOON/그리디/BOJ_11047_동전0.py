import sys

# input = sys.stdin.readline().rstrip()

n, m = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

cnt = 0
sum = 0

money.sort(reverse=True)

for i in range(n):

    if m >= money[i]:
        cnt += m // money[i]
        m %= money[i]


print(cnt)
