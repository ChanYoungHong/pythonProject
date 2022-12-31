n = int(input())
array = []
for i in range(n):
    array.append(input())


result = list(set(array))

sort_word = []
for i in result:
    sort_word.insert(len(i), len(i))

print(sort_word)
#
# result = []
# for j in range(n):
#     for k in range(j+1):
#         result.insert(j, len(array[k]))
#
# print(array)
# print(result)