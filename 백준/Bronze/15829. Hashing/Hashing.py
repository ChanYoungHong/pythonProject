L = int(input())
string = input()

dic = {}
for i in range(26):
    dic[97 + i] = i + 1
sum = 0

for i in range(L):
    sum += (dic[ord(string[i])]) * (31 ** i)

print(sum % 1234567891)