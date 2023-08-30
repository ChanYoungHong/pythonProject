import sys

input = sys.stdin.readline

'''
1.  
2. 
3.
4.

'''

left, right = input().split()
word = input().rstrip()

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'

xl, yl, xr, yr = None, None, None, None

for i in range(len(keyboard)):
    if left in keyboard[i]:
        xl = i
        yl = keyboard[i].index(left)

    if right in keyboard[i]:
        xr = i
        yr = keyboard[i].index(right)


time = 0
for ss in word:
    time += 1

    if ss in mo:
        for i in range(len(keyboard)):
            if ss in keyboard[i]:
                nx = i
                ny = keyboard[i].index(ss)

                time += abs(xr - nx) + abs(yr - ny)
                xr, yr = nx, ny
                break

    else:

        for i in range(len(keyboard)):
            if ss in keyboard[i]:
                nx = i
                ny = keyboard[i].index(ss)

                time += abs(xl - nx) + abs(yl - ny)
                xl, yl = nx,ny
                break

print(time)
