import sys, math

input = sys.stdin.readline

a,b,v = map(int, input().rstrip().split())

day = (v-b) / (a-b)
print(math.ceil(day))