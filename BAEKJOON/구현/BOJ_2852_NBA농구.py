import sys

input = sys.stdin.readline

n = int(input())

def time2num(strTime):

    hour, min = strTime.split(':')

    hour = int(hour) * 60
    min = int(min)

    return hour + min


def num2time(time):

    hour = str(time // 60)
    min = str(time%60)

    if len(hour) == 1:
        hour = '0'+hour

    if len(min) == 1:
        min = '0'+min

    return hour + ':' + min

timeDict = {}

for _ in range(n):
    teamNo, strTime = input().split()
    # teamDict[teamNo] = time2num(strTime)
    timeDict[time2num(strTime)] = int(teamNo)

# print(time2num('16:30'))
# print(num2time(990))

team1win = 0
team2win = 0

team1score = 0
team2score = 0

for i in range(time2num('48:00')):

    if i in timeDict:
        if timeDict[i] == 1:
            team1score += 1
        else:
            team2score += 1

    if team1score > team2score:
        team1win += 1
    elif team1score < team2score:
        team2win += 1

print(num2time(team1win))
print(num2time(team2win))





