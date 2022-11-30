import sys

#결론적으로 input() 내장 함수는 sys.stdin.readline()과
# 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.

input = sys.stdin.readline

cnt = int(input())

for i in range(cnt):
    a,b = map(int, input().split())
    print(a+b)