import sys
from collections import Counter

input = sys.stdin.readline



'''
1. 시간 복잡도 50인 것 같음
2. 짝수이면, 홀수이면 비교 
3. 짝수일 때, 양 옆에 같아질 때 까지 반복문을 돌리는 방법 ?
4. 
'''

word = input().rstrip()
check_word = Counter(word)

# print(check_word)

cnt = 0
result = ''
mid = ''

for k,v in check_word.items():

    if v % 2 == 1:
        cnt += 1
        mid = k

        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in sorted(check_word.items()):
    result += (k * (v // 2))

print(result + mid + result[::-1])