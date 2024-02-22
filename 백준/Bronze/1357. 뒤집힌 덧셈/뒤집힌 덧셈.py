
import sys

input = sys.stdin.readline


x,y = input().split()


res = ''
for i in x[::-1]:
    res += str(i)

res = int(res)
# print('res :', res)

res2 = ''
for j in y[::-1]:
    res2 += str(j)
res2 = int(res2)

# print('res 2:', res2)

total = (res + res2)
# print(type(total))

total = str(total)
# print(total[::-1])
total = int(str(total[::-1]))
print(total)



