import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
node = [[], [0,0]]

for i in range(n-1):
    kind, nums, connection = input().split()
    tree[int(connection)].append(i+2)
    node.append([kind, int(nums)])

def dfs(v):

    result = 0

    for i in tree[v]:
        result += dfs(i)

    if node[v][0] == 'W':
        result -= node[v][1]

        if result < 0:
            result = 0

    else:
        result += node[v][1]

    return result

print(dfs(1))
print(tree)
print(node)