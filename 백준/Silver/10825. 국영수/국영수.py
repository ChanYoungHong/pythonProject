import sys

input = sys.stdin.readline

n = int(input())

'''
1. 국어점수가 감소하는 순서
2. 국어가 같으면 영어가 증가
3. 국어 영어가 같으면 수학이 감소

'''
check = []
for _ in range(n):
    name, kr, en, mat = input().split()
    kr, en, math = map(int, (kr, en, mat))
    check.append((name, kr, en, math))

a_check = sorted(check, key=lambda x: (-x[1], x[2], -x[3], x[0]))


for i in a_check:
    print(i[0])