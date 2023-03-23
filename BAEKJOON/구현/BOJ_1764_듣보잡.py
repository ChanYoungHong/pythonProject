import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [ ]
for i in range(n):
    a.append(input().rstrip())

b = []
for j in range(m):
    b.append(input().rstrip())

a.sort()
b.sort()

def bs(start, end, target):

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] < target:
            start = mid + 1
        elif a[mid] > target:
            end = mid - 1
    return False


result = []
for i in b:
    if bs(0, len(a)-1, i):
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)