import sys

input = sys.stdin.readline

'''
1. 반복되는 숫자가 없게 방 번호를 만들려고 한다
2. 

'''

while 1:

    num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    try:
        n, m = map(int, input().splti())
    except:
        break

    total = (m - n) + 1
    cnt = 0
    for i in range(n, m + 1):
        test = str(i)
        flag = 0
        for j in num:

            if (test.count(j) >= 2):
                flag = 1

        if (flag == 1):
            cnt += 1

    total = total - cnt
    print(total)

# num = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
#
#
# for i in range(1, 10):
#     print(num[i])
