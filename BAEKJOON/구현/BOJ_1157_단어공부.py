'''

1. 시간복잡도 -
2. 아이디어  - 리스트를 만들어서 각각 인덱스를 돌려서 검사하는 방법
-> count() 함수를 사용해서 가장 큰 수를 뽑은 후 그 수를 대문자로 바꿔주기


'''

import sys

# input = sys.stdin.readline

words = input().upper()
array = list(set(words))

cnt_array = []
for i in array:
    cnt = words.count(i)
    cnt_array.append(cnt)

if cnt_array.count(max(cnt_array)) > 1:
    print('?')
else:
    max_index = cnt_array.index(max(cnt_array))
    print(array[max_index])

