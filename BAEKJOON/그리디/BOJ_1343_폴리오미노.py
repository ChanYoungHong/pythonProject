import sys

input = sys.stdin.readline

word = input()

word = word.replace('XXXX', 'AAAA')
word = word.replace('XX', 'BB')

if 'X' in word:
    print(-1)
else:
    print(word)
