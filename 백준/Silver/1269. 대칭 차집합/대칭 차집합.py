import sys

input = sys.stdin.readline

a,b = map(int, input().split())

alist = set(map(int, input().split()))
blist = set(map(int, input().split()))

answer1 = alist.difference(blist)
answer2 = blist.difference(alist)


print(len(answer1) + len(answer2))