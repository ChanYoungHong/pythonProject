
n = int(input())
def fibbonachi(n):

    if n == 0:
        return 1
    return n * fibbonachi(n-1)


print(fibbonachi(n))
