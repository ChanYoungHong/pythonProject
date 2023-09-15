import sys

input = sys.stdin.readline

n, k = map(int, input().split())

standard = []
rest = []
for _ in range(n):
    team = list(map(int, input().split()))

    if team[0] == k:
        standard = team
    else:
        rest.append(team)

rank = 1
for i in range(len(rest)):

    if rest[i][1] > standard[1]:
        rank += 1

    elif rest[i][1] == standard[1]:
        if rest[i][2] > standard[2]:
            rank += 1

        elif rest[i][2] == standard[2]:
            if rest[i][3] > standard[3]:
                rank += 1

print(rank)
