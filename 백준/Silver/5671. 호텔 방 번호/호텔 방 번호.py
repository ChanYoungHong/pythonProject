import sys

input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    total = (m - n) + 1
    cnt = 0
    for i in range(n, m + 1):
        test = str(i)
        flag = 0
        for j in set(test):
            if test.count(j) >= 2:
                flag = 1
        if flag == 1:
            cnt += 1

    print(total - cnt)