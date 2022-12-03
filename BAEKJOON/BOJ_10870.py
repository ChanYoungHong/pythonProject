


def fibonnaccchi(N):
    if N <= 1:
        return N
    return fibonnaccchi(N-1) + fibonnaccchi(N-2)


N = int(input())
print(fibonnaccchi(10))