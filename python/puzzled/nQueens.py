
def nQueens(n):
    board = [0 for _ in range(n)]
    nQueens_helper(n, 0, board)


def nQueens_helper(n, current, board):
    if n == current:
        print_board(board)
        return True

    for i in range(n):
        b = board[:]
        b[current] = i
        if isValid(n, current, b):
            nQueens_helper(n, current+1, b)


def isValid(n, current, board):
    for i in range(current):
        if board[i] == board[current]:
            return False

        if abs(board[i] - board[current]) == current - i:
            return False

    return True


def print_board(board):
    transposed = []
    width = len(board)
    for c in board:
        column = []
        for r in range(width):
            if c == r:
                column.append('Q')
            else:
                column.append('.')
        transposed.append(column)

    for row in zip(*transposed):
        print(*row)

    print()


if __name__ == '__main__':
    print('n=4')
    nQueens(4)
    print()
    print('n=8')
    nQueens(8)
