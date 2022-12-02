#
# N = int(input())
#
# # 앞 뒤가 같은지 팰린드롭인 문자열인지 확인을 해야 함? -> How ???
# # 반복문을 2개 돌려서 이게 그에 해당하는 수인지 확인한다 ?
#
# word = input()
#
# def recursion(word, l, r):
#
#     if l >= r: return 1
#     elif word[l] != word[r]: return 0
#     else: return recursion(word, l+1, r-1)
#
# def isPalindrome():
#     return recursion(word, 0, len(word)-1)
#
#
# print('ABBA', isPalindrome("ABBA"));
# print('ABC:', isPalindrome("ABC"));


#답을 보고 문제를 품
import sys
input = sys.stdin.readline


def recursion(s, l, r):
    global cnt  # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
    cnt += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)


# def recursion(s, l, r):
#     if l >= r:
#         return 1
#     elif s[l] != s[r]:
#         return 0
#     else:
#         return recursion(s, l + 1, r - 1)
#
#
# def isPalindrome(s):
#     return recursion(s, 0, len(s) - 1)
#
# for _ in range(int(input())):
#     cnt = 0
#     print(isPalindrome(input().rstrip()), cnt)기

# 답 보고 품

