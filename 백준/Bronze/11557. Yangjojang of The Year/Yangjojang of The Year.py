import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    temp = []
    for _ in range(n):
        S, L = input().rstrip().split()
        temp.append((S,int(L)))

        # print(temp)
    c = sorted(temp, key=lambda x : x[1], reverse = True)

    print(c[0][0])

