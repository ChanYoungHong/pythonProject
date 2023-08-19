import sys


input = sys.stdin.readline

check = ['a', 'e', 'i', 'o', 'u']

while True:

    word = input().rstrip()

    if word == 'end':
        break

    v_cnt, c_cnt = 0,0
    cnt = 0
    flag = True
    last = ''

    for i in word:

        # 조건 1 모음 하나를 반드시 포함하여야 한다.
        if i in check:

            # 모음이 'e' 또는 'o'가 아니면서 이전 글자와 같다면
            if v_cnt == 2 or ((i != 'e' and i != 'o') and last == i):
                flag = False
                break
            else:
                v_cnt += 1
                c_cnt = 0
                cnt += 1
                last = i

        else:
            # last를 두는 이유는 같은 글자가 연속적으로 나오는 것을 막기 위해서이다.
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



