n = int(input())
array = list(map(int, input().split()))

array.sort()

sum = 0
for i in range(n): # 0 1 2 3 4
    for j in range(i+1):
        sum += array[j]

print(sum)