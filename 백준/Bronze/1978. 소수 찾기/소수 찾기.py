import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in nums:
    error = 0
    
    if i > 1:
        
        for j in range(2, i):
            
            if i%j == 0:
                error += 1
        
        if error == 0:
            cnt += 1

print(cnt)

