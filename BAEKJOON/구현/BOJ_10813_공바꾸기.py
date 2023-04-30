import sys

input = sys.stdin.readline

'''
<포인트>

1. 바구니에 공이 1개씩 들어있음
2. 바구니 번호와 공의 번호가 같은게 들어감
3. M번 바꿀거임
4. 두 바구니의 공을 서로 교환한다.

'''

n,m = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(i)

for i in range(m): # 1 2 3 4 5
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(arr)


