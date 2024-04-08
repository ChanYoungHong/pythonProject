# import sys
#
# input = sys.stdin.readline
#
# '''
# 1부터 n까지에 수에 대해 차례로
# [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop]
# 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
# '''
#
# n = int(input())
#
# check = []
# answer = []
# for i in range(1, n+1):
#
#     num = int(input())
#     check.append(num)
#     print('check : ', check)
#
#     print('+')
#     answer.append(i)
#
#     print('answer : ', answer)
#     if answer[i-1] == num:
#         print('-')
#         answer.pop()
#     elif num in answer:
#         print('-')
#         answer.pop()
#
#
#


count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)