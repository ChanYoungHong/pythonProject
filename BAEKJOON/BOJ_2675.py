#
# 수도코드
#
# 1. N에 테스트케이스 개수를 입력을 받는다
# 2. R번 반복해서 문자열 P를 만들어서 출력한다.
# 3. num 횟수만큼 ABC 순서대로 넣고 반복하여 준다.
# 4. 각각의 index의 자리를 3번씩 반복 해줘야 한다.
# 5.

# t = int(input())
#
# result = "";
# for i in range(t):
#     num, s = input().split()
#
#     for j in num:       #              #          0 1 2
#         result += s[j]                  #         A B C
#     print(result)


# 블로그 답안
# t = int(input())
# text = ''
# for i in range(t):
#     num, s = input().split()
#     for i in s:
#         text += int(num) * i # 처음에 i가 s의 길이만큼 올라가는데 어떻게 같은 문자가 반복이 가능한가 ? 라고 생각 함
#     print(text)

# a = "charlie"
# result = ''
#
# for k in a: # 문자열을 넘으면 k 자리에 그 해당하는 문자열 index 0 1 2 3 4 차례대로 들어 감
#     result += int(2) * k # 2 * k
#     print(result)





n = int(input())
answer = ''

for i in range(n):
    num, word = input().split()
    for j in word:
        answer += int(num) * j
    print(answer)
























