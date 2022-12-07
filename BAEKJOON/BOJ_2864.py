# 수도코드
# 1. a, b 를 받을 때 5 또는 6이 있는지 확인한다
# 2. 5 또는 6을 포함하는 수가 있으면 문자열에 포함하는지 확인해서 뽑고
# 3. 다시 그 5 또는 6으로 바꾼 후에 더해서
# 4. 더 한 값들을 전부 다 리스트에 담는다
# 5. 리스트에 담긴 수들 중에서 max, min 값을 도출해낸다
# 6.
#
#
#
#
# a, b= map(int, input().split())
# sum = a + b
#
# list = []
#
# strA = str(a)
# strB = str(b)
#
# print(strA)
# print(strB)
#
# # if strA.contains("5"):
# #     return "5가 존재합니다"
#
# chageStrB = strB.replace(strB, "26")
# print(chageStrB)




a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min, max)


