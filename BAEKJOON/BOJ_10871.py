a,b = map(int, input().split())

array = list(map(int, input().split()))

for i in range(a):
    # 조건에 5가 들어가는 것이 아니라 b가 들어가야 함
    # 그래서 계속 틀림
    if array[i] < b:
        print(array[i], end = ' ')
    else:
        continue