import sys

input = sys.stdin.readline


'''
1. 약수를 구하기
2.
'''

tmp = 1

while True:
    n = int(input())

    if n == -1:
        break

    nums = []
    for i in range(1, n+1):
        if n % i == 0:
            nums.append(i)

        if i == n:
            nums.pop()

    check = nums
    if sum(check) == n:
        print(n, " = ", " + ".join(str(i) for i in check), sep="")
    else:
        print(n,"is NOT perfect.")
