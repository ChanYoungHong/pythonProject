품
# 재귀함수 헷갈림
# 시간 - 20분

def ffibonnaccchi(N):
    if N <= 1:
        return N
    return ffibonnaccchi(N-1) + ffibonnaccchi(N-2)

N = int(input())
print(ffibonnaccchi(N))


