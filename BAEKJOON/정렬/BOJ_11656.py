s = input()

# array = []
# # for i in range(len(s)):
# array.append(s[1:])
# array.append(s)
# array.append(s[2:])
# array.append(s[4:])
# array.append(s[3:])
# array.append(s[-1])
# array.append(s[-2:])
# array.append(s[-3:])

array = []

for _ in s:
    array.append(s)
    s = s[1:]

array.sort()
for i in array:
    print(i)