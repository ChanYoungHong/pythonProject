n1 = int(input())
card = list(map(int, input().split()))

n2 = int(input())
check = list(map(int, input().split()))

card.sort()

def binary_search(card, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if card[mid] == target:
            return mid
        elif card[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return None

for i in range(n2):
    if binary_search(card, check[i], 0, n1 - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')