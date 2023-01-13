'''

1. 반복문을 두 개 돌려서 하나씩 비교하는 방법으로 생각 함
2. 오른쪽 값을 기준으로 왼쪽 값을 넣었을 때 그 길이가 오른쪽 값의 길이와 같으면 애니그램으로 출력

'''

import sys

input = sys.stdin.readline

n = int(input().rstrip())

array1 = []
array2 = []

for _ in range(n):
    a, b = map(str, input().split())

    x = list(a)
    y = list(b)

    x.sort()
    y.sort()

    if x == y:
        print("%s & %s are anagrams." % (a, b))
    else:
        print("%s & %s are NOT anagrams." % (a, b))
