import sys

input = sys.stdin.readline

'''
1. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
2.  “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 

'''

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    floor = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]

    print(floor[-1])