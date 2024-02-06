import sys

input = sys.stdin.readline

n = int(input())
seat = input().rstrip()
seat = seat.replace('LL', 'X')

if 'X' in seat:
    print(len(seat) + 1)
else:
    print(len(seat))