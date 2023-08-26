import sys

input = sys.stdin.readline

n = int(input())

fileDict = {}
ans = []

for _ in range(n):
    word = input().rstrip().split('.')
    ans.append(word[1])

for i in ans:
    if i not in fileDict:
        fileDict[i] = 0
    fileDict[i] += 1

ddic = sorted(fileDict.items())

print(ddic)

for a,b in ddic.items():
    print(a,b)
