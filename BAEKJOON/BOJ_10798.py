
# array = list(input())
# text = ""
#
# print(array)


#
# 1. [i,j] 2차원 배열로 받으면 j를 고정 시켜야 된다고 생각했다.
# 2. i 번째 위치를 하나씩 올리면서 값을 도출 -> 세로이기 때문에
# 3.
#
#

words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

text = ''
for i in range(max(length)): # 6
    for j in range(5): # 0 1 2 3 4
        if i < length[j]: #
            text += words[j][i]

print(length)
print(text)
