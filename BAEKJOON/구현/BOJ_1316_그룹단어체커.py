n = int(input())

answer = 0

for _ in range(n):
    a = input()

    cnt = 0
    for i in range(len(a) - 1):

        if a[i] != a[i + 1]:
            new_a = a[i+1:]
            print('a[i+1]', a[i+1])
            if new_a.count(a[i]) > 0:
                cnt += 1

    if cnt == 0:
        answer += 1

print(answer)