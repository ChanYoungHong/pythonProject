import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ranking = []
standard = []
for _ in range(n):

    arr = list(map(int, input().rstrip().split()))

    if arr[0] != m:
        ranking.append(arr)
    else:
        standard = arr
        # standard.append(arr)

cnt = 1

for j in range(len(ranking)):

    if ranking[j][1] > standard[1]:
        cnt += 1
    elif ranking[j][1] == standard[1]:
        if ranking[j][2] > standard[2]:
            cnt += 1
        elif ranking[j][2] == standard[2]:
            if ranking[j][3] > standard[3]:
                cnt += 1

print(cnt)