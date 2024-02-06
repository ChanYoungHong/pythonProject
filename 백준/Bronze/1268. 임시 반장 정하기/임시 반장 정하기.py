import sys

input = sys.stdin.readline

'''
1. 1-5학년까지 가장 같은 반을 많이 한 학생을 임시반장으로
2. 

'''
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# check = []
# up = 0
# for i in range(n):
#     for j in range(n-1):
#         print('i : ', i)
#         print('j+1 : ', j+1)
#         if board[j][i] == board[j+1][]:
#             check.append(i+1)
#             check.append(j+1)
#     print(check)

answer = [[0 for _ in range(n)] for _ in range(n)]

for k in range(5):
    for i in range(n):
        for j in range(i+1, n):
            if board[i][k] == board[j][k]:
                answer[i][j] = 1
                answer[j][i] = 1

count = []
for a in answer:
    count.append(a.count(1))

print(count.index(max(count)) + 1)