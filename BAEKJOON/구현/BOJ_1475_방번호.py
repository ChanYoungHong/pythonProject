import sys

input = sys.stdin.readline
'''
1. 아이디어 
2. 시간복잡도 - 
3. 
'''
n = input().rstrip()

sett = [0] * 9

for i in n:

    idx = int(i)

    if idx == 9:
        idx = 6
    sett[idx] += 1

sett[6] = (sett[6] + 1) // 2
print(max(sett))


