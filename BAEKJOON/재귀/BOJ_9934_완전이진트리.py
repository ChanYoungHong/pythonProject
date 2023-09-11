import sys

input = sys.stdin.readline

'''
1. 시간 복잡도 및 풀이 방향 찾기
2. 범위가 1 10 사이라서 그냥 일반적인 구현으로 풀이 가능할 듯
3. 상근이는 빌딩에 들어 간 순서대로 종이에 적었다
4. 트리 문제이니 dfsf를 사용함 
5. 왼쪽 자식을 가지고 있지 않거나, 이미 들어갔다면 현재 노드 빌딩에
들어가고 종이를 번호에 적는다
6. 

방문 순서 -> 부모 - 왼 - 오 방식으로 진행 됨

'''

# k = int(input())
# b_num = list(map(int, input().split()))
#
# node = (2**k) - 1
# paper = []
#
# tree = [[] for _ in range(node)]
# visited = [[] for _ in range(node)]
#
# def dfs(lev):
#
#
#
#     dfs(lev + 1)
#
#
#
#     return
#
#
# print(tree)

k = int(input())
inorder = list(map(int, input().split()))

answer = [[] for _ in range(k)]


def dfs(inorder, dep):

    mid = (len(inorder) // 2)
    answer[dep].append(inorder[mid])

    if len(inorder) == 1:
        return

    dfs(inorder[:mid], dep + 1)
    dfs(inorder[mid + 1:], dep + 1)


dfs(inorder, 0)

for i in answer:
    print(*i)

print('answer : ', answer)
