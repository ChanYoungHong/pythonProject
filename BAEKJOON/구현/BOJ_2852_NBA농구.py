import sys

input = sys.stdin.readline

# 시간 -> 숫자로 환산
def timeToNum(strTime):
    hour, min = map(int, strTime.split(':'))
    return hour * 60 + min


# 숫자 -> 시간으로 환산
def numToTime(ttime):

    hour = str(ttime // 60)
    min = str(ttime % 60)

    if len(hour) == 1:
        hour = '0'+hour

    if len(min) == 1:
        min = '0' + min
    return hour + ':' + min

scoreDict = {}

n = int(input())
for _ in range(n):
    teamNo, strTime = input().split()
    scoreDict[timeToNum(strTime)] = int(teamNo)

team1win = 0
team2win = 0

team1score = 0
team2score = 0

# print(scoreDict)
for i in range(timeToNum('48:00')):

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

