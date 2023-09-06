import sys
input = sys.stdin.readline

'''

풀어 나가는 방향성은 ?
-> 더하는 기준의 길이를 1씩 높여 나가면서 모든 경우의 수를 다 더해서 

새로운 배열을 거기 만들어서 넣은 후에 max()로 꺼내기 ?
약간 슬라이딩 윈도우 같은 느낌으로 ?

이전까지 모든 숫자의 합 중 최대값을 구하여라.
'''

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(n-1):

    dp.append(max(dp[i]+arr[i+1], arr[i+1]))

print(max(dp))
