import sys

input = sys.stdin.readline

'''
1. 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다.
2.
3.
4.

5
100 99 98
100 97 92
63 89 63 -> 0 89 0 -> 89점
99 99 99 -> 0 0 0 -> 0점
89 97 98 ->
'''

n = int(input())
temp = [[],[], []]
score = [0] * n
for _ in range(n):

    t = list(map(int, input().split()))
    temp[0].append(t[0])
    temp[1].append(t[1])
    temp[2].append(t[2])


for i in range(3):
    for j in range(n):

        if temp[i].count(temp[i][j]) > 1:
            score[j] += 0
        else:
            score[j] += temp[i][j]


for i in score:
    print(i)