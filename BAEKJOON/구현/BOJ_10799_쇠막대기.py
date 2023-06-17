import sys

input = sys.stdin.readline

'''

레이저 -> ()를 뜻함, 
2. 

')'가 나오면 두가지 경우로 나누어진다.
')'가 나오고 이전 문자가 '('이었다면 해당 파트는 레이저이다. 따라서 현재 stack에 쌓인 '('개수(=쇠막대기 개수)만큼 개수를 더해준다.
')'가 나오고 이전 문자도 ')'이었다면 쇠막대기 끄트머리에 대한 표현이다. 따라서 하나가 나올때마다 하나씩만 추가해주면 된다.
문제풀이 자체는 어렵지 않았지만 문제이해에 오래걸렸던 문제이다. 코딩테스트의 문제 중엔 이보다 훨씬 복잡한 문제가 많으니 문제이해능력 자체도 키울 필요성이 있겠다.
'''

lazer = list(input().rstrip())

ans = 0
st = []

for i in range(len(lazer)):

    if lazer[i] == '(':
        st.append('(')
        print('st1 : ', st)
    else:
        if lazer[i-1] == '(':
            st.pop()
            ans += len(st)
            print('st :', st)
            print('ans : ', ans)
        else:
            st.pop()
            ans += 1
            print('ans2 : ', ans)

print(ans)

