import sys

input = sys.stdin.readline

'''
1. 어떤 방식으로 코드를 짤 지 고민
2. 부등호의 기준에 맞게 숫자 하나씩 다 넣어봐야할 듯
3. 

'''


visited = [0] * 10

def check(i,j,k):

    if k == '<':
        return i < j
    else:
        return i > j

def dfs(dep, s):

    global max_ans, min_ans

    if (n+1 == dep):

        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if not visited[i]:
            if (dep == 0 or check(s[-1], str(i), rule[dep-1])):
                visited[i] = True
                dfs(dep + 1, s + str(i))
                visited[i] = False



min_ans = ''
max_ans = ''
n = int(input())
rule = input().split()

dfs(0, '')
print(max_ans)
print(min_ans)


