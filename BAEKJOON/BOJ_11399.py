
n = int(input())
array = list(map(int, input().split()))
result = 0

array.sort()
for i in range(n):
    for j in range(i+1):
        result += array[j]

print(result)