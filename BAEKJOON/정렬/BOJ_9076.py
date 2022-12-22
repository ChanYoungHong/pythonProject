n = int(input())

for _ in range(n):
    array = list(map(int, input().split()))
    array.sort()

    if array[3] - array[1] >= 4:
        print('KIN')
    else:
        print(sum(array[1:4]))


