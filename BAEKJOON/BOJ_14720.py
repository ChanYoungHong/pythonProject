# 수도 코드
#
# 1. n으로 값을 받는다
# 2. array list 형태로 값을 입력 받는다
# 3. 0, 1, 2 순서대로 받도록 한다
# 4. 순서대로인지 검증 후에 cnt로 값으로 올려서 최대값을 구한다
#
#
# 0 1 2 순서대로 와야 하니깐, cnt % 3 == 0
#
#
N = int(input())
array = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if array[i%3 == 0]:
        cnt += 1
    elif array[i%3 == 1]:
        cnt += 1
    elif array[i%3 == 2]:
        cnt += 1

print(cnt)

# 답 참고 함
# n = int(input())
# milk = list(map(int,input().split()))
#
# count = 0
#
# for i in range(n):
#     if milk[i] == count % 3:
#         count += 1
#
# print(count)



