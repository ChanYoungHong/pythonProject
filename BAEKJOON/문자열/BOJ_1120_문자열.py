import sys

input = sys.stdin.readline


'''

1. 알고리즘 - 
2. 시간복잡도 - 따로 알고리즘 필요 없을 듯 웬만하면 다 됨
3. 어떤 방식? - 
'''

word1, word2 = input().split()
res = []

for i in range(len(word2) - len(word1) + 1):
    cnt = 0

    for j in range(len(word1)):
        if word1[j] != word2[i+j]:
            cnt += 1

    res.append(cnt)

# print(res)
print(min(res))


