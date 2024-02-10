import sys

input = sys.stdin.readline
'''
1. 모든 행 또는 열이 .으로 되어있는 부분들을 체크
2. 대각선으로 검증이 가장 효율적이고 빠르다고 판단 
3. 현재 있는 위치가 .일 때, 가로 세로를 확인하기
4. 

'''
n,m = map(int, input().split())
board = []

result1 = 0
for i in range(n):
    tmp = input().rstrip()
#    print('tmp : ', tmp)
    board.append(tmp)
#    print('board : ', board)

    if 'X' not in tmp:
        result1 += 1


#print('board : ', board)
result2 = 0
# 0 1 2 3 4 5 6 7
for i in range(m):
    cnt2 = 0
    
    # 0 1 2 3 4
    for j in range(n):
        if board[j][i] == 'X':
            break
        else:
            cnt2 += 1

    if cnt2 == n:
        result2 += 1


print(max(result1, result2))