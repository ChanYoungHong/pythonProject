'''

1. 시간복잡도 -
2. 아이디어 -

'''

word = input()

word = word.replace('XXXX', 'AAAA')
word = word.replace('XX', 'BB')

if 'X' in word:
    print(-1)
else:
    print(word)
# temp = 0
# for i in range(len(word)):
#     if word[i] == '.':
#         word[i] = '.'
#     elif (len(word) % 2) == 0:
#         if len(word) % 4 == 0:
#             word[len(word) - 4] = 'A'
#         elif len(word) % 2 == 0:
#             word[len(word)-2:0] = 'B'
#
# print(''.join(map(str, word)))