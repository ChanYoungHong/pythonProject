'''

1. 시간복잡도 -
2. 아이디어 -

'''

import sys

for _ in range(int(input())):
    a = list(map(int, input().split()))
    case, li = a[0], a[1:]
    res = 0
    for i in range(1, 20):
        m, m_idx = max(li)+1, i
        for j in range(i):
            if li[j] > li[i] and li[j] < m:
                m = li[j]
                m_idx = j
        if m_idx != i:
            li = li[:m_idx] + [li[i]] + li[m_idx:i] + li[i+1:]
            res += i-m_idx
    print(case, res)

    # for i in range(n):
    #     case = array[0]
    #     student = array[1:]
    #     res = 0
    #
    #     for j in range(1, 20):
    #         if student[j] > student[j]

    ''' case의 1을 사용하려면 어떻게 해야하나 ?'''
