import sys

input = sys.stdin.readline

word = input().rstrip()
word = word.upper()

arr = list(set(word))

print('arr : ', arr)
check = []
for i in arr:
    check.append(word.count(i))

print('check : ', check)
if check.count(max(check)) > 1:
    print('?')

else:
    max_index = check.index(max(check))
    print(arr[max_index])