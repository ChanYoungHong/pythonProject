import sys

input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))
arr = sorted(set(nums))

dic = {arr[i] : i for i in range(len(arr))}

for i in nums:
    print(dic[i], end=' ')