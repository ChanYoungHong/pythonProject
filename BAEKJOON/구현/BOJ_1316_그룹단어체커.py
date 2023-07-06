import sys

input = sys.stdin.readline

'''
1. 아이디어 - 2중 for문 돌려서 -> new_word.count()를 사용하기 -> 
0보다 큰 거 개수 따로 새기 cnt, ans로 나눠서
cnt == 0일 때 ans += 1해주기

2. 시간복잡도 - 적당한 3중 루프 다 돌아감
3. 문법 - 
'''

t = int(input())

ans = 0
for _ in range(t):

    word = input()
    cnt = 0
    for i in range(len(word) - 1):

        if word[i] != word[i+1]:
            new_word = word[i+1:]

            if new_word.count(word[i]) > 0:
                cnt += 1

    if cnt == 0:
        ans += 1

print(ans)

