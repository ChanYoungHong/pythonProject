import sys

input = sys.stdin.readline


n = int(input())

arr = set()
for _ in range(n):
    word = input().rstrip()
    arr.add(word)


ans = []
for i in arr:
    ans.append((len(i), i))

# print(ans)

ans.sort()

for a,b in ans:
    print(b)


