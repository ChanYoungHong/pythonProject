import sys

input = sys.stdin.readline


'''
111222..333444555.... // 길이 3인 널빤지
.MMMMM..MMMM.MMMM.... // 웅덩이
012345678901234567890 // 좌표

어떻게 하면 물울덩이를 덮을 수 있을까? 

1. 쩜을 만날때 i+2까지 확인하기 만약 M이면 널판지 사용하기 ?
2. 

'''

N,L = map(int, input().split())

sand = []

for i in range(N):
    start, end = map(int, input().split())
    sand.append([start, end])


sand.sort(key = lambda x:x[1], reverse=True)

cnt = 0
last_index = sand[0][1]

for start, end in sand:

    if last_index < start:
        continue

    if last_index < end:
        end = last_index

    len = end - start
    remain = len % L

    if remain == 0:
        last_index = start
        cnt += len // L

    else:
        last_index = start - L + remain
        cnt += len // L + 1

print(cnt)

# water = '.....................'
#
# for k in range(N):
#
#     a,b = map(int, input().split())
#
#     for i in range(a,b):
#
#         water[i] = 'K'
#
#     print(water)



# cnt = 1
# result = 0
# for i in range(len(water)):
#
#     if water[i+2] == 'M' and water[i+1] != '.':
#         water[i] = 1
#         cnt += 1
#
#     if cnt == 3:
#         result += 1
#
# print(result)
# print(water)





