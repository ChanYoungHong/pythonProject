import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
S = input().rstrip()

check = 'IOI' * n

answer, i, count = 0,0,0

while i < (m-1):

    if S[i:i+3] == 'IOI':
        i += 2
        count += 1

        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)


# print(S.count(check)+1)

# cnt = 0
# for i in range(len(S) - len(check)):
#     for j in range(len(S)):
#
#         if S[i] +  == check:
#             cnt += 1
#         print(S[i + 2])
#
# print(cnt)

# S = S.replace(check, 'I')
#
# S = S.replace(check, 'I')

# print(S)
# print(len(S) - 1)
