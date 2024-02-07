import sys

input = sys.stdin.readline




while True:

    board = list(map(int, input().split()))
    if board[0] == 0:
        break
    else:
        n = board[0]

        check_board = board[1:]
        result = []

        # for value in check_board:
        #     if value not in result:
        #         result.append(value)

        for i in check_board:

            if len(result) == 0:
                result.append(i)
            elif result[-1] != i:
                result.append(i)

        result.append('$')
        print(*result)