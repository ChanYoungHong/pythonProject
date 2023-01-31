
word = input()

alb = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = []
for i in alb:
    word = word.replace(i, "1")

print(len(word))
