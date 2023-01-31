
import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a,b))


# array = sorted(array, key=lambda x:x[0])
# array = sorted(array, key=lambda x:x[1])
ranking = []
for i in range(n):
    cnt = 0
    for j in range(n):

        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            cnt += 1
    ranking.append(cnt + 1)

print(*ranking)

        # if array[i][0] > array[i+1][0] and array[i][1] > array[i+1][1]:
        #     ranking.append(1)
        # elif array[i][0] > array[i+1][0] or array[i][1] > array[i+1][1]:
        #     ranking.append(2)
        # else:
        #     ranking.append(5)


