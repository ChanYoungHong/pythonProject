import sys

input = sys.stdin.readline


n = int(input())
word = input()

num = ''
val = 0

for i in word:
    if '0' <= i and i <= '9':
        num += i
    elif num != '':
        val += int(num)
        num = ''

if num != '':
    val += int(num)

print(val)