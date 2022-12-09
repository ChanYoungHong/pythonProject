n = int(input())
array = [[0] * 100 for _ in range(100)]

cnt = 0

for i in range(n):
    a,b = map(int, input().split())

    for j in range(a, a+10):
        for k in range(b, b+10):
            array[j][k] = 1


for z in array:
    cnt += z.count(1)

print(cnt)