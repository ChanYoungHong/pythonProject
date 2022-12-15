n = int(input())
array = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if array[i] == cnt % 3:
        cnt += 1
print(cnt)
