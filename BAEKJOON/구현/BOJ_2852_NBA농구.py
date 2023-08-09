import sys

input = sys.stdin.readline

n = int(input())

def timeToNum(strTime):
    min, sec = map(int, strTime.split(":"))
    return min * 60 + sec

def numToTime(num):
    min = str(num // 60)
    sec = str(num % 60)

    if len(min) == 1:
        min = "0" + min

    if len(sec) == 1:
        sec = "0" + sec

    return min + ":" + sec


scoreDict = {}

for i in range(n):
    teamNo, strTime = input().split()
    scoreDict[timeToNum(strTime)] = int(teamNo)


team1win = 0
team2win = 0
team1score = 0
team2score = 0

print(scoreDict)
for i in range(timeToNum("48:00")):

    if i in scoreDict:
        if scoreDict[i] == 1:
            team1score += 1
        else:
            team2score += 1

    if team1score > team2score:
        team1win += 1
    elif team1score < team2score:
        team2win += 1

print(numToTime(team1win))
print(numToTime(team2win))