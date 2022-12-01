
# cnt = 0
#
# for i in range(10):
#     GeneralNum = int(input())
#     if (GeneralNum % 42) != 0:
#         cnt += 1
#     else:
#         cnt = 0
# print(cnt)


# set 함수를 사용하는 이유는 set 중복 값을 없애준다.
nlist=[]
for i in range(10):
    num= int(input())
    nlist.append(num % 42)

print(len(set(nlist)))
