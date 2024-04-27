import sys

input = sys.stdin.readline

# while True:
#
#     word1, word2 = map(str, input().split())
#
#
#     if word1 in word2:
#         print('Yes')
#     else:
#         print('No')
#
#
#     for i in word2:
#         for j in word1:
#
#             if i == j:


while True:
    try:
        s, t = input().split()

        value = 0
        flag = 0
        for i in range(len(t)):
            if t[i] == s[value]:
                value += 1
                if value == len(s):
                    flag = 1
                    break

        if flag == 1:
            print('Yes')
        else:
            print('No')

    except:
        break

