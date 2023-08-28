import sys

input = sys.stdin.readline

'''
1. 일직선상의 코스들을 모두 지나 끝까지 도달한 뒤에, 다시 출발 지점으로 복귀
2. 이동 거리가 K일 때, 현재 지나고 있는 코스의 번호를 출력하는 프로그램
3. 

'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))


# ans = (sum(arr) * 2) - k
#
# temp = 0
# for i in range(len(arr)):
#
#     temp += arr[i]
#
#     if temp >= ans:
#         print(i+1)
#         break

for i in range(n):
    k -= arr[i]

    if k < 0:
        print(i+1)
        break
else:
    for i in range(n-1, -1, -1):
        k -= arr[i]
        if k < 0:
            print(i+1)
            break


