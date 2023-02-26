from collections import defaultdict

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

answer = []
tempArr = []
res = []

report = list(set(report))
user = defaultdict(set)
cnt = defaultdict(int)

for r in report:
    a, b = r.split()
    user[a].add(b)
    cnt[b] += 1

print(user)

for i in id_list:
    result = 0
    for u in user[i]:
        if cnt[u] >= k:
            result += 1
    answer.append(result)

print(answer)

#     for i in range(len(report)):
#         tempArr += report[i].split(' ')

#     for i in range(len(tempArr)):

#         if i % 2 == 1:
#             res.append(tempArr[i])
#         else:
#             continue


#     for i in id_list:

#         answer.append(res.count(i))

#     answer.sort(reverse = True)
