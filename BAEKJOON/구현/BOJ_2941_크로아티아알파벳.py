import sys

input = sys.stdin.readline

zz = input().rstrip()

word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in word:

    zz = zz.replace(i, '*')

print(len(zz))
