import sys

input = sys.stdin.readline

n = int(input())

# for i in range(n):
#     for j in range(n-1, 3-i, -1): # 0 ~ 4:
#         print("i = ", i)
#         print("j = ", j)
#         # print("*", end="")
#
#         if i == 0 and j ==
#     print()

for i in range(1, n+1): # 1 2 3 4 5
    print(" " * (n-i) + "*" * i)