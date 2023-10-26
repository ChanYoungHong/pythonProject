import sys

input = sys.stdin.readline

n = int(input())

exist = []
for _ in range(n):

    word = input().rstrip().split(' ')
    flag = False

    for i in range(len(word)):

        if word[i][0].upper() not in exist:
            exist.append(word[i][0].upper())
            flag = True
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            print(' '.join(word))
            # 첫 글자를 발견한 후 루프를 종료하고 다음 단어로 이동하도록 합니다.
            break

    if not flag:

        for i in range(len(word)):
            check = False
            for j in range(len(word[i])):

                if word[i][j].upper() not in exist:
                    exist.append(word[i][j].upper())
                    flag = True
                    check = True
                    word[i] = word[i][:j] + '[' + word[i][j] + ']' + word[i][j + 1:]
                    print(' '.join(word))
                    # 내부 루프를 종료하고 바깥 루프로 넘어갈 때 사용 됨
                    break

            if check == True:
                break

    if not flag:
        print(' '.join(word))
