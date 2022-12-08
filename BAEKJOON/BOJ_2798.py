a, b = map(int, input().split())
array = list(map(int, input().split()))
answer = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(i+2, a):
            if b < array[i]+array[j]+array[k]:
                continue
            else:
                answer = max(answer, array[i]+array[j]+array[k])

print(answer)
