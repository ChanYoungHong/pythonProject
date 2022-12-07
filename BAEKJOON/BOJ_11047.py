
# 10, 4200
n, m = list(map(int, input().split()))
array = []
answer = 0

for i in range(n):
    nums = int(input())
    array.append(nums)
    array.sort(reverse=True)

    # if m >= array[i]:                # for문 하나로 돌리게 되면 배열에 하나 밖에 담겨 있어서 출력이 안 됨, 그래서 for문 2개를 사용해야 함
    #     answer += m // array[i]
    #     m %= array[i]
    #     print(array[i])

for j in range(n):
    if m >= array[j]:  # for문 하나로 돌리게 되면 배열에 하나 밖에 담겨 있어서 출력이 안 됨, 그래서 for문 2개를 사용해야 함
        answer += m // array[j]
        m %= array[j]

print(answer)
print(array)