import sys

input = sys.stdin.readline

word1, word2 = input().rstrip().split()

a, b = len(word1), len(word2)

res =[ ]

cnt = 0
for i in range(b - a + 1): # 0 1
    for j in range(a): # 0 1 2 3 4 5

        if word1[j] != word2[i+j]:
            # print('word1 : ', word1[i+j], end = '  ')
            # print('word2 : ', word2[i+j])
            cnt += 1
    res.append(cnt)
    cnt = 0

print(min(res))
print(res)