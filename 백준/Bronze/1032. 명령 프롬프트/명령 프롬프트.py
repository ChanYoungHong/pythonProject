n = int(input())
filename = []

for _ in range(n):
    a = input()
    filename.append(a)

result = list(filename[0])

for i in range(n):
    for j in range(len(result)):

        if result[j] == filename[i][j]:
            continue
        else:
            result[j] = '?'

print(''.join(result))