import sys

input = sys.stdin.readline

n = int(input())
test_dict = {}
for _ in range(n):
    word = input().rstrip().split('.')

    for i in word:

        if word[1] not in test_dict:
            test_dict[word[1]] = 0
    test_dict[word[1]] += 1

# print(test_dict)

test_dict = sorted(test_dict.items())

for a,b in test_dict:
    print(a,b)

