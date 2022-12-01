# 12월 1일(목) - 다시 문제 풀어보기
# 겹치는 부분을 빼야 하는데 어떻게 처리 함?

# 내가 작성했던 코드
# cnt = int(input())
#
# size = 0
#
# for i in range(cnt):
#     n, k = map(int, input().split())
#     size = (n+10) * (k+10)
#     print(size)

# 다른 블로그의 답변


array = [[0] * 100 for _ in range(100)] # 리스트에 값을 다 0으로 초기화 한다.

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1 # 색칠이 되는 부분들이 다 값 1로 초기화 됨

cnt = 0
for row in array:
    cnt += row.count(1) # row에 1이 몇 개 있는지 확인 할 수 있다, 특정 한 값 데이터 개수 세기
                        # count함수 -> 특정한 값을 가지는 데이터 개수를 셀 때 사용한다

print(cnt)