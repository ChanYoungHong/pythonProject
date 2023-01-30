
word = input()


sum = 0
alb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alb:
    word = word.replace(i, '*')

print(len(word))