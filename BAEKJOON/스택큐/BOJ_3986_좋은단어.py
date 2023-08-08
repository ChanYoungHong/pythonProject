import sys

input = sys.stdin.readline

n = int(input())

'''
-> 교차 하지 않도록, 선을 잇는 방법은 ?? 
'''

cnt = 0

for i in range(n):
    word = input().rstrip()
    arr = []

    for j in range(len(word)):

        if arr:
            if word[j] == arr[-1]:
                arr.pop()
            else:
                arr.append(word[j])
        else:
            arr.append(word[j])

    if not arr:
        cnt += 1

print(cnt)

