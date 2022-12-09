# 12월 3일 복습
# N = int(input())

# def fac(N):
#
#     if N == 0:
#         return 1
#
#     return N * fac(N-1)
#
# print(fac(N))

def solution(n):
    # 1.
    if n > 0:
        return n
    else:
        return 1

    # 2.
    if n == 0:
        return 1

    return n * solution(n-1)


print(solution(10))
print(solution(0))
print(solution(1))
