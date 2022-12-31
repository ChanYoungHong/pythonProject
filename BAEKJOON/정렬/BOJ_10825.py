# n = int(input())
#
# array = []
# for i in range(n):
#     array.append(list(map(str, input().split())))
#
# for i in range(n):  # 0 1 2 3 4 5 6
#
#     if array[i][1] == array[i + 1][1]:
#         array[i][2].sort()
#     elif array[i][1] == array[i][2]:
#         array[i][3].sort(reverse=True)
#     elif array[i][1] == array[i][2] and array[i][2] == array[i][3]:
#         array.sort()
#     else:
#         array[i][1].sort()
#
#     print(array[i][0])

n = int(input())

students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])