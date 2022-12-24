
array = []

for i in range(5):
    array.append(int(input()))

array.sort()

sum = 0
for j in array:
    sum += j
sum = (sum // len(array))


print(sum)
print(array[2])
