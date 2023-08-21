import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

arrDict = {}

for i in arr:
    if i not in arrDict:
        arrDict[i] = 0
    arrDict[i] += 1

arrDict = sorted(arrDict.items(), key=lambda x:x[1], reverse=True)

for a,b in arrDict:
    for j in range(b):
        print(a, end = ' ')