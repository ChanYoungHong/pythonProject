import sys

input = sys.stdin.readline

'''
1. 첫 글자자가 이미 단축키로 되어 있는지 확인
2. 첫 글자가 되어 있다면, 안 된 것이 있다면 단축키로 지정한다.
3. 아무것도 단축키로 지정 못 하면, 그냥 놔두고 
4. 1번 ~ N번째 옵션까지 차례대로 적용
'''

n = int(input())

save_key = []
for _ in range(n):

    word = list(input().split())

    for i in range(len(word)):

        if word[i][0].upper() not in save_key:
            save_key.append(word[i][0].upper())
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            print(' '.join(word))
            break

    else:

        for z in range(len(word)):
            flag = False

            for k in range(len(word[z])):

                if word[z][k].upper() not in save_key:
                    save_key.append(word[z][k].upper())
                    flag = True
                    word[z] = word[z][:k] + '[' + word[z][k] + ']' + word[z][k+1:]
                    print(' '.join(word))
                    break

            if flag:
                break

        else:
            print(*word)



