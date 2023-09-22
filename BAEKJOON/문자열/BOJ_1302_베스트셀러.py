import sys

input = sys.stdin.readline

'''
1. 알고리즘 - 가장 많이 팔린 책을 구하기, 사전 순으로 출력을 해줘야 함
2. 시간복잡도 - 1000보다 작을 때, 공식 상 벨만 포드인데..
3. 배열? - dict 너리를 써서 카운트 해줘야 할 것 같은, 아니면 itertools
'''

n = int(input())

temp = {}
for _ in range(n):
    word = input().rstrip()

    if word not in temp:
        temp[word] = 0
    temp[word] += 1

# print(temp)

# d1 = sorted(temp.items())
# print(d1)

print(temp)
d2 = sorted(temp.items())
print(temp)
# print(d2)
big = 0
for k,v in d2:

    if v > big:
        big = v
        maxxxx = k

print(maxxxx)
