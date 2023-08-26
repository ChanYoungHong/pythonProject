import sys

input = sys.stdin.readline

'''
1. 첫 글자자가 이미 단축키로 되어 있는지 확인
2. 첫 글자가 되어 있다면, 안 된 것이 있다면 단축키로 지정한다.
3. 아무것도 단축키로 지정 못 하면, 그냥 놔두고 
4. 1번 ~ N번째 옵션까지 차례대로 적용
'''

n = int(input())

save_Key = []
# for _ in range(n):
#
#     sKey = input().rstrip()
#     if sKey[0] not in save_Key:
#         save_Key.append(sKey[0])
#
#     # 첫 글자가 단축키로 저장이 되어 있다면
#     elif sKey[0] in save_Key:
#
#         # 모든 단어 중에서 안 된 단어를 저장해라
#         for i in sKey:
#             if i not in save_Key:
#                 save_Key.append(i)
#
#     print(save_Key)

for _ in range(n):
    Key = list(map(str, input().rstrip().split()))
    print('Key : ', Key)

    for i in range(len(Key)):
        if Key[i][0].upper() not in save_Key:
            save_Key.append(Key[i][0].upper())
            Key[i] = '[' + Key[i][0] + ']' + Key[i][1:]
            print(' '.join(Key))
            break

    else:

        print('len(Key) : ', len(Key))

        for j in range(len(Key)):
            flag = False
            for k in range(len(Key[j])):

                print('len(Key[j]) : ', len(Key[j]))

                if Key[j][k].upper() not in save_Key:
                    save_Key.append(Key[j][k].upper())
                    print('save_Key : ', save_Key)
                    flag = True
                    Key[j] = Key[j][:k] + '[' + Key[j][k] + ']' + Key[j][k+1:]
                    print('Key[j][:k] : ', Key[j][:k])
                    print('Key[j][:k]222 : ', Key[j][k])
                    print('Key[j][:k]3333 : ', Key[j][k+1:])
                    print(' '.join(Key))
                    break
            if flag:
                break

        else:
            print(*Key)
