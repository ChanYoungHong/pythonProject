import sys, math

input = sys.stdin.readline

'''
1. 가장 큰 값과 작은 값들을 제외하고 평균을 낸다
2. 
'''


ans = []

def sss(val):

    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(input().rstrip())

if n:
    nums = []
    for _ in range(n):
        nums.append(int(input().rstrip()))

    stand = sss(n*0.15)
    nums.sort()

    if stand > 0:
        print(sss(sum(nums[stand:-stand])/len(nums[stand:-stand])))
    else:
        print(sss(sum(nums) / len(nums)))
else:
    print(0)

