import sys

input = sys.stdin.readline


n,m = map(int, input().split())

arr1 = set()
for i in range(n):

    arr1.add(input().rstrip())

arr2 = set()

for i in range(m):
    arr2.add(input().rstrip())

ans = set(arr1 & arr2)


# print(arr1)
# print(arr2)
# print(ans)

print(len(ans))
for i in sorted(ans):
    print(i)