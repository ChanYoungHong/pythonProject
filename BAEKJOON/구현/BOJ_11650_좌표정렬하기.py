import sys

input = sys.stdin.readline

n = int(input())


arr1 = []
arr2 = []

for i in range(n):
    a,b = map(int, input().split())

    arr1.append((a,b))

arr1 = sorted(arr1, key=lambda x:(x[0], x[1]))

for a,b in arr1:
    print(a,b)

