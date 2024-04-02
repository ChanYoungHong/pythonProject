n,m = map(int,input().split(' '))

s = list()
o = list()

for _ in range(m):
    a,b = input().split(' ')
    s.append(int(a))
    o.append(int(b))

# 세트 가격
s = min(s)

# 낱개 가격
o = min(o)

if s < o * 6:
    if s < (n % 6) * o:
        print((n // 6) * s + s)
    else:
        print((n // 6) * s + (n % 6) * o)

elif s >= o * 6:
    print(n * o)