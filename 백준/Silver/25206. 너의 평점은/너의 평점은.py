import sys

input = sys.stdin.readline

'''
1. 전공평점은 -> 학점 x 과목평점
2. P인 과목은 계산에서 제외해야 함
3. 

'''

grade = []
hakjum = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

grade_points = {
    'A+': 4.5,
    'A': 4.0,
    'A0': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'B0': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'C0': 2.0,
    'D+': 1.5,
    'D': 1.0,
    'D0': 1.0,
    'F': 0.0,
    'P': None  # Assuming P is for Pass, so no grade point value assigned
}

total = 0.0
t_credit = 0.0
for i in range(20):

    sub, credit, grade = input().rstrip().split()
    # print(sub, credit, grade)

    if grade == 'A+':
        total += (float(credit) * hakjum[0])
        t_credit += float(credit)
    elif grade == 'A0':
        total += (float(credit) * hakjum[1])
        t_credit += float(credit)
    elif grade == 'B+':
        total += (float(credit) * hakjum[2])
        t_credit += float(credit)
    elif grade == 'B0':
        total += (float(credit) * hakjum[3])
        t_credit += float(credit)
    elif grade == 'C+':
        total += (float(credit) * hakjum[4])
        t_credit += float(credit)
    elif grade == 'C0':
        total += (float(credit) * hakjum[5])
        t_credit += float(credit)
    elif grade == 'D+':
        total += (float(credit) * hakjum[6])
        t_credit += float(credit)
    elif grade == 'D0':
        total += (float(credit) * hakjum[7])
        t_credit += float(credit)
    elif grade == 'F':
        total += (float(credit) * hakjum[8])
        t_credit += float(credit)
    elif grade == 'P':
        continue

    # total = (total//20)
# print(total // 20)
# print('t_credit : ', t_credit)
# print('total : ', total)
total = (total / t_credit)
total = round(total, 6)

print(total)
