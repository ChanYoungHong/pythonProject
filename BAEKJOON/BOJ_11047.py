n, m = map(int, input().split())
array = []
cnt = 0
result = 0

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(n):
    if m >= array[i]:
        cnt += (m // array[i])
        m %= array[i]


print(cnt)
print(result)
