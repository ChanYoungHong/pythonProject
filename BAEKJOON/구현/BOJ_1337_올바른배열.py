import sys

input = sys.stdin.readline

'''
1. ans의 길이를 구하여라
2. 길이가 5개인 연속적인 수를 구하여라
3. 계획 첫 번째 입력되는 값에서부터 5개를 골라서 있는지 없는지 확인해서 개수를 구하기

'''

n = int(input())

arr = []
temp = []

arr = [int(input()) for _ in range(n)]

for i in range(n):
    cnt = 0

    for j in range(arr[i], arr[i]+5):

        if j not in arr:
            cnt += 1
    temp.append(cnt)

print(min(temp))