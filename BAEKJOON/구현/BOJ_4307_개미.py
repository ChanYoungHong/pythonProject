import sys

input = sys.stdin.readline


locat = []
t = int(input())

for i in range(t):
    stick, ant = map(int, input().rstrip().split())

    min_time = []
    max_time = []

    for j in range(ant):

        # locat.append(stick)
        loc = int(input())

        min_time.append(min(loc, stick - loc))
        print('mIn_time : ', min_time)

        max_time.append(max(loc, stick - loc))
        print('mAx_time : ', max_time)

    print(max(min_time), max(max_time))

