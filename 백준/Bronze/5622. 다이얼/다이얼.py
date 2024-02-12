import sys

input = sys.stdin.readline

'''
1. 숫자를 하나 누르면 다디얼이 처음으로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 
다시 돌려야 한다.
2.
3.
4.


'''

# num = [[],[],[],[],[],[],[],[],[],[]]
# alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

# num[0].append('')
# num[1].append(alph[:3])
# num[2].append(alph[3:6])
# num[3].append(alph[6:9])
# num[4].append(alph[9:12])
# num[5].append(alph[12:15])
# num[6].append(alph[15:19])
# num[7].append(alph[19:22])
# num[8].append(alph[22:26])
# num[9].append('')


a = input()

for i in range(len(a)):
    for j in dial:

        if a[i] in j:
            time += dial.index(j) + 3

print(time)