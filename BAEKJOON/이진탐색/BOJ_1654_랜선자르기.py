
'''

n < 1,000,000 아래면 nlogn으로 찾아야 된다. 그러므로 이진탐색 or dp를 사용해야 함



'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = []
for _ in range(n):
    num.append(int(input().rstrip()))

start = 1
end = max(num)

while start <= end:

    mid = (start + end) // 2
    cnt = 0
    for i in num:

        if i >= m:
            cnt += (i // mid)


    if cnt >= m:
        start = mid + 1
    else:
        end = mid -1

print(end)


