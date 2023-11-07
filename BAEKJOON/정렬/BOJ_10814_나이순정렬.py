import sys

input = sys.stdin.readline

n = int(input())

orderDict = {}

ans = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    ans.append((age,name))

ans.sort(key=lambda x : (x[0]))
# ans = sorted(orderDict, key=lambda x : (x[0], x[1]))

for i,j in ans:
    print(i,j)