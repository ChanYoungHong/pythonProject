import sys

input = sys.stdin.readline

word = input().rstrip()

arr = list(word)

num = []
for i in arr:

    if i.isdigit():
       num.append(i)
       print('i', i)
       arr.remove(i)

num = list(map(int, num))
arr.sort()

ans = ''
for i in arr:
    ans += i

ans += str(sum(num))

print(sum(num))
print(arr)
print(ans)