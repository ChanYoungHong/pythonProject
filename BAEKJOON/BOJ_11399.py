N = int(input())
timeArray = list(map(int, input().split()))
resultTime = 0

timeArray.sort()
for i in range(N):
    for j in range(i+1):
        resultTime += timeArray[j]

print(resultTime)
