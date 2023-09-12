import sys
import collections

input = sys.stdin.readline



'''
1. 시간 복잡도 50인 것 같음
2. 짝수이면, 홀수이면 비교 
3. 짝수일 때, 양 옆에 같아질 때 까지 반복문을 돌리는 방법 ?
4. 
'''

word = input().rstrip()
check_word = collections.Counter(word)

cnt = 0
result = ''
mid = ''

print(check_word)
for k, v in list(check_word.items()):

    if v % 2 == 1: # 홀수라면
        cnt += 1
        mid = k # 중간에 들어갈 값으로 저장
        if cnt >= 2: # 홀수가 2개이상이면 팰린드롬이 될 수 없다 !!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()):
    result += (k * (v // 2))

print(result + mid + result[::-1])
print(result[::-1])