case = int(input())


def solve():
    string = input()
    validity = True
    if string[len(string)-1] == 'B':
        count = 0
        for i in range(0, len(string)):
            if string[i] == 'A':
                count += 1
            else:
                count += -1
                if count < 0:
                    validity = False
                    break
    else:
        validity = False

    print("YES") if validity else print("NO")


while case:
    solve()
    case += -1
