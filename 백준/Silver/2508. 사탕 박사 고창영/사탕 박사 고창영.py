import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    r, c = map(int, input().rstrip().split())
    box = []
    for i in range(r):
        box.append(input().rstrip())

    cnt = 0
    for y in range(r):
        for z in range(c-2):

            if box[y][z] == '>' and box[y][z+1] == 'o' and box[y][z+2] == '<':
                cnt += 1

    for y in range(r-2):
        for z in range(c):

            if box[y][z] == 'v' and box[y + 1][z] == 'o' and box[y+2][z] == '^':
                cnt += 1

    print(cnt)
