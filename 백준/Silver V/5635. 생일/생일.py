import sys

input = sys.stdin.readline

'''
1. 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 
2. 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.

'''

n = int(input())

person = []
for i in range(n):
    name, dd, mm, yyyy = input().rstrip().split()
    dd,mm,yyyy = map(int, (dd,mm,yyyy))
    person.append((yyyy, mm, dd, name))

person.sort()

print(person[-1][3])
print(person[0][3])