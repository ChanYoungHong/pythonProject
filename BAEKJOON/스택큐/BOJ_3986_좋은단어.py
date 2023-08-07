import sys

input = sys.stdin.readline

n = int(input())

'''
-> 교차 하지 않도록, 선을 잇는 방법은 ?? 
'''


cnt = 0
for _ in range(n):
    word = input().rstrip()
    arr = []

    for i in range(len(word)):
        if arr:
            if word[i] == arr[-1]:
                # print('word[-1] : ', word[-1])
                arr.pop()
            else:
                arr.append(word[i])
        else: # 비어 있다면
            arr.append(word[i])

    if not arr:
        cnt += 1

print(cnt)