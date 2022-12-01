
N = int(input())
wordList = []

for i in range(N):
    word = input()
    wordList.append(word)

# set으로 중복을 제거 해야하는 것은 이해완료
set_word = list(set(wordList))

# 여기서부터 어떻게 해야 할 지 모르겠음
sort_word = []
for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)

    # wordList.sort(reverse=True)
    # wordList.sort()
    # if len(wordList[i]) == len(wordList[i+1]):
    #     wordList.sort()
    # elif len(wordList[i]) > len(wordList[i+1]):
    #     wordList.sort()
    # else:
    #     continue
    # print(set_word[i])