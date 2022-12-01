
# 값 일력 받는 곳
N = int(input())

array = []

for i in range(N):
    numbers = int(input())
    array.append(numbers) # 배열에 담기

for i in range(N):
    array.sort() # 오름차순으로 정렬 후 프린트
    print(array[i])

# 풀이시간 20분 걸림
# for문 2번 사용하고 싶지 않았음, 아니면 재귀를 이용해서 푸는 건 ?!