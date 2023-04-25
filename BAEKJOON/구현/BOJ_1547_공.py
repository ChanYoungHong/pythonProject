import sys

input = sys.stdin.readline

m = int(input())

cup = [0] * 3
cup[0] = 1

for _ in range(m):

    a, b = map(int, input().split())
    cup[a-1], cup[b-1] = cup[b-1], cup[a-1]

print(cup.index(1)+1)
