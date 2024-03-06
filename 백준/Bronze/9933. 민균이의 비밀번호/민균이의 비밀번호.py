import sys

input = sys.stdin.readline

'''
1. 모든 단어의 길이가 홀수라는 사실
2. 
'''

n = int(input())

temp = []
for i in range(n):

    word = input().rstrip()
    temp.append(word[::-1])

    for j in temp:
        if j == word:
            print(len(word), word[len(word)//2])