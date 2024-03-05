import sys

input = sys.stdin.readline

tree = list(map(int, input().split()))
answer = [1,2,3,4,5]
while tree != answer:

    # if tree[0] > tree[1]:
    #     tree[0], tree[1] = tree[1], tree[0]
    #     print(*tree)
    # elif tree[1] > tree[2]:
    #     tree[1], tree[2] = tree[2], tree[1]
    #     print(*tree)
    # elif tree[2] > tree[3]:
    #     tree[2], tree[3] = tree[3], tree[2]
    #     print(*tree)
    # elif tree[3] > tree[4]:
    #     tree[3], tree[4] = tree[4], tree[3]
    #     print(*tree)

        # if tree == answer:
        #     break

    for i in range(len(tree) - 1):
        if tree[i] > tree[i+1]:
            tree[i], tree[i+1] = tree[i+1], tree[i]
            print(*tree)