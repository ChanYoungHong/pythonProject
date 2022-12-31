n = int(input())  # 5개 상근이 가진 카드
array1 = list(map(int, input().split()))

m = int(input())  # 8개 상근이 가졌는지 확인해야 할 카드
array2 = list(map(int, input().split()))

array1.sort()


def binary_search(array1, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array1[mid] == target:
            return mid
        elif array1[mid] > target:
            end = mid - 1
        else:
            start = start + 1

    return None

for i in range(m):
    if binary_search(array1,array2[i],0,n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
