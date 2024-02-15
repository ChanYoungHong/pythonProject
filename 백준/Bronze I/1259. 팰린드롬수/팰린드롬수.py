import sys

input = sys.stdin.readline


while True:


    n = int(input())

    if n == 0:
        # print('finish')
        break

    str_n = str(n)

    # 짝수일 때
    if len(str_n)%2 == 0:
        rest = 0
        rest = len(str_n) // 2

        front = str_n[:rest]
        back = str_n[rest:]
        back = back[::-1]
        
        if front == back:
            print('yes')
        else:
            print('no')
        
        # print('rest : ', rest)
        # print('front : ', front)
        # print('back : ', back)

    # 홀수일 때
    elif len(str_n)%2 == 1:
        rest = 0
        rest = len(str_n) // 2

        front = str_n[:rest]
        back = str_n[rest+1:]

        back = back[::-1]

        if front == back:
            print('yes')
        else:
            print('no')

    # print(rest)
    # print(front)
    # print(back)