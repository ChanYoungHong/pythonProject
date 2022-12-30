n = int(input())

for _ in range(n):
    a, b = input().split()

    result = ''
    for i in b:
        result += i * int(a)
    print(result)





