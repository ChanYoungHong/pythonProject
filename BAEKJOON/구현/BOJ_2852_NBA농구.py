import sys

input = sys.stdin.readline

n = int(input())


# 시간 -> 초로 환산
def timeToNum(strTime):

    min, sec = map(int, strTime.split(":"))
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

team1Win = 0
team2Win = 0

teamScore1 = 0
teamScore2 = 0

for k in range(timeToNum("48:00")):

    if k in scoreDict:
        if scoreDict[k] == 1:
            teamScore1 += 1
        else:
            teamScore2 += 1

    if teamScore1 > teamScore2:
        team1Win += 1
    elif teamScore1 < teamScore2:
        team2Win += 1

print(numToTime(team1Win))
print(numToTime(team2Win))