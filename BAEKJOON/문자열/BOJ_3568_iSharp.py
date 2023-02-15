import sys

input = sys.stdin.readline

words = list(map(str, input().split()))

fun = words[0]
other = words[1:]

for i in other:

    new_words = i.replace(' ', '').replace(',', '').replace(';', '')

    print(fun, end='')
    for j in range(len(new_words)-1, 0, -1):

        if not new_words[j].isalpha():

            if new_words[j] == '[':
                print(']', end='')
            elif new_words[j] == ']':
                print('[', end='')
            else:
                print(new_words[j], end='')

    print(' ', end='')
    for k in range(len(new_words)):
        if new_words[k].isalpha():
            print(new_words[k], end='')

    print(';')

