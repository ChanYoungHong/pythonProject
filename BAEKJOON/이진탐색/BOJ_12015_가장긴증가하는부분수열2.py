import sys

input = sys.stdin.readline

'''
1. 어떤 방식으로 이진탐색을 할 지 찾아보기
2. 
'''

n = int(input())
arr = list(map(int, input().split()))

# dp = [1] * n

# for i in range(n):
#     for j in range(i):
#
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)

dp = [0]

for i in range(n):
    low = 0
    high = len(dp) - 1

    while low <= high:

        mid = (low + high) // 2
        print('mid', mid)
        if dp[mid] < arr[i]:
            low = mid + 1
        else:
            high = mid - 1

    print('low :', low)
    if low >= len(dp):
        print('arr[i] :', arr[i])
        dp.append(arr[i])
    else:
        dp[low] = arr[i]

print(len(dp) - 1)
print(dp)


