
# array = list(input().split())


list = []

for i in range(9):
    list.append(int(input()))

print(max(list))

# 최대값 몇 번째 인덱스에 있는지 확인하는 방법
print(list.index(max(list))+1)

