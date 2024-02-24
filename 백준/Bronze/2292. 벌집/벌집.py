import sys

input = sys.stdin.readline

'''

1. 1 -> 6 -> 12 -> 18 -> 24


'''

n = int(input())

pileup = 1
cnt = 1

while n > pileup:

    pileup += 6 * cnt
    cnt += 1

print(cnt)