import sys

input = sys.stdin.readline

'''
1. 씨앗이 3개 뿐임
2. 모든 경우의 수를 구해서 그 LIST를 하나 만들어서 최솟값 구하는 방식으로 하기
3. 
'''

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최소 비용을 구하기 위한 저장소
def check(i,j, visited):
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj) in visited:
            return False
    return True

def dfs(visited, total):
    global answer

    if total >= answer:
        return

    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if check(i,j,visited) and (i,j) not in visited:
                    temp = [(i,j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni,nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

# def seeddd(cnt):
#
#     if seed == 3:
#
#         return
#
#     for i in range(n):
#         for j in range(n):
#
#             if board[i][j] == 0:
#

n = int(input())
answer = int(1e9)
fields = [list(map(int, input().split())) for _ in range(n)]
dfs([], 0)

print(answer)