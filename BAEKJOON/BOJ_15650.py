
n, m = list(map(int, input().split()))
result = []

def fff(start):
    if len(result) == m: # 1 == 2
        print(" ".join(map(str, result)))
        return

    for i in range(start, n+1): # (1, 5) // 1 2 3 4
        if i not in result:
            result.append(i)
            fff(i+1)
            result.pop()

fff(1)




