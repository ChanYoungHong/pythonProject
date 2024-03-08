import sys

input = sys.stdin.readline

'''
1. 풀기 시작한 시간부터 경과한 시간과 난이도로 결정한다

'''

nums = []
for i in range(8):

    a = int(input())
    nums.append((a,i+1))

nums = sorted(nums, key=lambda x : x[0], reverse = True)

cnt = 0
total = 0
temp = []
for k,z in nums:


    if cnt == 5:
        break
    total += k
    temp.append(z)
    cnt += 1

print(total)
temp.sort()
print(*temp)