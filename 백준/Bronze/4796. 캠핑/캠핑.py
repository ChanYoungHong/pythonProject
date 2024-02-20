import sys

input = sys.stdin.readline

'''
1. 20일 중 10일 동안만 사용할 수 있음
2. 8이 연속되지 않으면 5일을 가장 많이 나올 수 있는 경우의 수를 구하여라
3.
4.


'''
cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    ans = V // P
    res = V % P
    
    if L < res:
        res = L

    print('Case %d: %d' %(cnt, ans*L+res))

    cnt += 1



