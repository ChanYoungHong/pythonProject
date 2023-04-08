import sys

input = sys.stdin.readline

# card_n = int(input())
# # cards = [0]
# cards = [0] + list(map(int,input().split()))
#
# # for i in range(card_n):
# #     cards.append(int(input().split()))
#
# dp = [0] * card_n
#
# # print(cards)
# for i in range(1, len(cards)):
#
#     if card_n % i == 0:
#         dp.append((card_n // i) * cards[i])
#
# print(max(dp))

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])


print(dp[i])
print(dp)
print(p)