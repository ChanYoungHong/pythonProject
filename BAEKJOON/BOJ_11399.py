
# 2 5 1 4 3이 되어야 함

#사람 1 2 3 4 5
#시간 3 1 4 3 2

n = int(input())
a = list(map(int, input().split()))

a.sort()
result = 0

for i in range(n): # 0
    for j in range(i+1):
        result += a[j]

print(result)





