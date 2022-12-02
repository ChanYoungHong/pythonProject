# N = int(input())
#
# # 내 답안
# for i in range(1, 10):
#     def add(N):
#         return N * (N - i)
#         sum += add(N)
#
# print(sum)

# 블로그 답안
def fac(n):
    result = 1
    if n > 0:
        result = n * fac(n-1)
    return result

n = int(input())
print(fac(n))

# 15분 정도 걸림, 답 보고 품