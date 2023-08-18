import sys

input = sys.stdin.readline

n = int(input())


# 시간 -> 초로 환산
def timeToNum(strTime):
    min, sec = map(int, strTime.split(':'))
    return min * 60 + sec

# 초 -> 시간으로 환산
def numToTime(time):

    min = str(time // 60)
    sec = str(time % 60)

    if len(min) == 1:
        min = '0' + min

    if len(sec) == 1:
        sec = '0' + sec

    return min + ':' + sec

scoreDict = {}

for i in range(n):
    teamNo, strTime = input().split()
    scoreDict[timeToNum(strTime)] = int(teamNo)

teamWinTime1 = 0
teamWinTime2 = 0
teamScore1 = 0
teamScore2 = 0


for j in range(timeToNum('48:00')):

    if j in scoreDict:
        if scoreDict[j] == 1:
            teamScore1 += 1
        else:
            teamScore2 += 1


    if teamScore1 > teamScore2:
        teamWinTime1 += 1
    elif teamScore1 < teamScore2:
        teamWinTime2 += 1

print(numToTime(teamWinTime1))
print(numToTime(teamWinTime2))