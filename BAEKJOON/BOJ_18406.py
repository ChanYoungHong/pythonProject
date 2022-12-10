array = input()

sum1 = 0
sum2 = 0

intArray = list(map(int, array))

global mid
mid = int(len(array)) // 2

for i in range(mid):
    sum1 += intArray[i]

for i in range(mid, len(array)):
    sum2 += intArray[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

# for i in range(len(array)):

    # mid = int((len(array))) // 2
    # sum1 += intArray[i:mid]
    # sum1 += int(array[i:mid])
    # sum2 += int(array[mid:len(array)])

    # if array[i:mid] == array[mid:len(array)]:
    #     print("LUCKY")
    # else:
    #     print("READY")
