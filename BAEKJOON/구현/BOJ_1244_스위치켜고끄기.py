import sys

input = sys.stdin.readline

'''
1. 1 -> 스위치 켜짐, 0 -> 꺼져 있음 
2. 남학생은 1, 여학생은 2
3. 남학생의 특징은 -> 자기가 받은 수의 배수이면, 그 스위치 상태를 바꾼다

4.
5.

'''

n = int(input())

switch = [0] + list(map(int, input().split()))
student = int(input())

# print('switch : ', switch)

def change(x):
    global switch
    switch[x] = abs(switch[x] - 1)


for _ in range(student):
    se, cnt = map(int, input().split())
    i = 1
    # 남학생꺼 먼저 해결하기
    if se == 1:

        # for i in range(1, len(switch)):
        #     if (i) % 3 == 0 and switch[i] == 0:
        #         switch[i] = 1
        #     elif (i) % 3 == 0 and switch[i] == 1:
        #         switch[i] = 0

        while cnt * i <= n:
            change(cnt * i)
            i += 1


    # 여학생꺼 해결하기
    elif se == 2:

        # for i in range(1, len(switch)):
        #
        #     if switch[i - 1] == switch[i + 1] and switch[i - 2] == switch[i + 2]:
        #         switch[i] = 0
        #         switch[i - 1] = 0
        #         switch[i + 1] = 0
        #         switch[i - 2] =

        change(3)
        while 1 <= cnt - i and cnt +i <= 8 and switch[cnt -i] == switch[cnt+i]:
            change(cnt-i)
            change(cnt+i)
            i += i

for i in range(1, n+1):
    print(switch[i], end = ' ')
    # if not i % 20:
    #     print()