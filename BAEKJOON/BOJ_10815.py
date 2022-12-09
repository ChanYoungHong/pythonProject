myNum = int(input())
myCard = list(map(int, input().split()))

yourNum = int(input())
yourDeck = list(map(int, input().split()))

myCard.sort() # -10 2 3 6 10

def binary_search(array, target,start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return mid + 1
        else:
            return mid - 1
    return None


# binary_search(myNum, yourDeck[i],0, myNum-1)
#
# for i in range(n):

