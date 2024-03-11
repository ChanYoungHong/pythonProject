import sys

input = sys.stdin.readline

'''
1. 산술평균 
2. 중앙값
3. 최빈값, 여러 개 있을 때 최반값 중 두 번째로 작은 값 출력하기
4. 최댓값과 최솟값의 차이
'''

n = int(input())

total = 0
nums = []
cnt_num = []
for i in range(1, n+1):

    num = int(input())
    nums.append(num)
    total += num

    # for j in range():

# 산술평균

nums.sort()
print(round(total/len(nums)))
print(nums[n//2])

dict = {}
for j in nums:

    if j not in dict:
        dict[j] = 1
    else:
        dict[j] += 1

max_cnt = max(dict.values())
max_arr = sorted([k for k,v in dict.items() if v == max_cnt])

if len(max_arr) > 1:
    print(max_arr[1])
else:
    print(max_arr[0])

print(max(nums) - min(nums))
