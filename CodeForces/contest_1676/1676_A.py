case = int(input())


def solve():
    ticket_raw = input()
    ticket = [ticket_raw[i] for i in range(0, 6)]
    td = [int(i) for i in ticket]
    if td[0] + td[1] + td[2] == td[3] + td[4] + td[5]:
        print("YES")
    else:
        print("NO")


while case:
    solve()
    case += -1
