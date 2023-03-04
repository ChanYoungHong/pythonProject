alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()


for i in alph:

    word = word.replace(i, '*')

print(len(word))

