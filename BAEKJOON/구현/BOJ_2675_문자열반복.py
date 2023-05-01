import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, word = input().rstrip().split()
    ans = ''
    for i in word:
        ans += int(n) * i
    print(ans)



# for i in range(3):
#     a = 'A' * i
#
# print(a)