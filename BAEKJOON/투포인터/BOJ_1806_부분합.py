import sys

input = sys.stdin.readline
'''

s 이상이면서 길이가 가장 짧은 것을 구해야 함
조건
1. s 이상이어야 함
2. 가장 짧은 구간을 구해야 함

시간복잡도 - 100,000 이진탐색이나, 누적 합 공식을 사용해야 할 듯

두 가지 공식을 섞어서 사용해야 할 것 같음
1. 이진탐색과 + 누적합 공시을 같이 사용함
2. 슬라이딩 윈도우?를 써야 할 듯
'''
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0,0
summ = 0
min_length = sys.maxsize


while True:

    # 합이 S보다 클 경우

    if summ > s:
        summ -= arr[left]
        min_length = min(min_length, right - left)
        left += 1

    elif right == n:
        break

    # 합이 S보다 작을 경우
    else:
        summ += arr[right]
        right += 1


if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)

# start = 0
# end = len(arr) - 1
# cnt = 0
#
#
#
# while start < end:
#
#     if arr[start] + arr[end] < s:
#         end -= 1
#     elif arr[start] + arr[end] > s:
#         start += 1
#         cnt += 1
#     else:
#         start += 1
#         end -= 1
#
# print(cnt)


# inter_num = 0
# end = 0
# cnt = 0
#
# for i in range(n):
#
#     while inter_num >= s and end < n:
#         inter_num += arr[end]
#         end += 1
#
#     if inter_num >= s:
#         cnt += 1
#
#     inter_num -= arr[i]
#
# print(cnt)
