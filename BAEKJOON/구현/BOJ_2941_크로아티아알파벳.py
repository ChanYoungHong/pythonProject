

import sys

input = sys.stdin.readline

alb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input().rstrip()


for i in alb:
    word = word.replace(i, '*')

print(len(word))