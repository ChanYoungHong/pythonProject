import sys

input = sys.stdin.readline


# 시간 -> 숫자로
def timeToNum(str):
    hour, min = map(int, str.split(':'))
    return hour * 60 + min


def numToTime(nnum):
    hour = str(nnum // 60)
    min = str(nnum % 60)

    if len(hour) == 1:
        hour =  '0' + hour

    if len(min) == 1:
        min =  '0' + min

    return hour + ':' + min

n = int(input())
teamDict = {}
for _ in range(n):
    teamNo, timeStr = map(str, input().rstrip().split())
    teamDict[timeToNum(timeStr)] = int(teamNo)


team1win = 0
team2win = 0

team1score = 0
team2score = 0

# print(teamDict)
# print(timeToNum('48:00'))
for i in range(timeToNum('48:00')):

    if i in teamDict:
        if teamDict[i] == 1:
            team1score += 1
        else:
            team2score += 1

    if team1score > team2score:
        team1win += 1
    elif team1score < team2score:
        team2win += 1

print(numToTime(team1win))
print(numToTime(team2win))



