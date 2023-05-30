import sys

input = sys.stdin.readline


word = list(input().rstrip())

sum = 0
arr = ''
arr2 = []

for i in word:

    if i.isdigit():
        sum += int(i)
    else:
        arr2.append(i)


arr2.sort()
print(''.join(arr2)+str(sum))

# word = word.sort()
# arr2 = arr.sort()
# print(arr.sort())
