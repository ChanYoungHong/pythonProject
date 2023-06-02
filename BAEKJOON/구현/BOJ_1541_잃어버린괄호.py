import sys

input = sys.stdin.readline

text = input().rstrip().split('-')

res = []
for i in text:

    e = i.split('+')
    tt = 0

    for j in e:

        tt += int(j)
    res.append(tt)


b = res[0]
for z in range(1, len(res)):
    # print('z :', z)
    b -= res[z]

print(b)



