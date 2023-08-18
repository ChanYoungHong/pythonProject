import sys


input = sys.stdin.readline

check = ['a', 'e', 'i', 'o', 'u']

while True:

    word = input().rstrip()

    if word == 'end':
        break

    # 자음과 모음
    # 모음 아 에 이 오 우

    v_cnt = 0
    c_cnt = 0
    last = ''
    flag = True
    cnt = 0

    for i in word:

        if i in check:

            if v_cnt == 2 or ((i != 'e' and i != 'o') and last == i):
                flag = False
                break
            else:
                v_cnt += 1
                c_cnt = 0
                cnt += 1
                last = i

        else:

            if c_cnt == 2 or last == i:
                flag = False
                break
            else:
                c_cnt += 1
                v_cnt = 0
                last = i

    if cnt == 0:
        flag = False

    # 주어진 조건이 참일 경우에는 if 안으로
    # 거짓일 경우에는 else로 감

    if flag:
        print("<{}> is acceptable.".format(word))
    else:
        print("<{}> is not acceptable.".format(word))



