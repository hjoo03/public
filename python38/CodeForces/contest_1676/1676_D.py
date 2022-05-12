case = int(input())


def solve():
    x_p, y_p = input().split()
    x_p = int(x_p)
    y_p = int(y_p)
    board = []
    for i in range(0, x_p):
        board.append([int(j) for j in input().split()])
    results = []

    def calc(x, y):
        s = board[x][y]

        # left_upward
        try:
            c = 1
            while x-c >= 0 and y+c >= 0:
                s += board[x-c][y+c]
                c += 1
        except IndexError:
            pass

        # left_downward
        try:
            c = 1
            while x-c >= 0 and y-c >= 0:
                s += board[x-c][y-c]
                c += 1
        except IndexError:
            pass

        # right_upward
        try:
            c = 1
            while x+c >= 0 and y+c >= 0:
                s += board[x+c][y+c]
                c += 1
        except IndexError:
            pass

        # right_downward
        try:
            c = 1
            while x+c >= 0 and y-c >= 0:
                s += board[x+c][y-c]
                c += 1
        except IndexError:
            pass

        return s

    for i in range(0, x_p):
        for j in range(0, y_p):
            res = calc(i, j)
            results.append(res)
    print(max(results))


while case:
    solve()
    case += -1
