import sys

# input = sys.stdin.readline

# n = input()
#
# # z = int(n)
# #
# # print(z)
#
# ex = n +
#
#
# if (n % 30) == 0:
#     print(n)
# else:
#     print(-1)

n = list(input())
n.sort(reverse=True)

sum = 0

for i in n:
    sum += int(i)

if sum % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))