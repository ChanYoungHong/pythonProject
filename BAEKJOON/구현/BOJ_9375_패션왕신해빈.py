import sys

input = sys.stdin.readline

'''
1. 한 번 입었던 옷들의 조합을 절대 다시 입지 않아야한다.
2. 같은 종류의 옷은 겹치지 않게 입혀야 한다.
'''

t = int(input())

for i in range(t):

    clothe = {}
    n = int(input())

    for j in range(n):
        v, k = input().split()

        if clothe.get(k) == None:
            print('kkk :', k)
            clothe[k] = set()
        clothe[k].add(v)

    print(';;;;', clothe.get(k))
    print('****', clothe)
    print('00000 : ', clothe.values())
    print('++++ : ', clothe.items())


    cnt = 1
    for key in clothe.keys():
        cnt *= len(clothe[key]) + 1
    print(cnt - 1)


# ans = dict()
#
# print(clothe)
# for k,v in clothe:
#     ans[v] = k
#
# print(ans)

# from collections import Counter
#
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     s = []
#
#     for j in range(n):
#         a,b = input().split()
#         s.append(b)
#     num = 1
#     result = Counter(s)
#     print(result)
#     for key in result:
#         num *= result[key] + 1
#     print(num - 1)
