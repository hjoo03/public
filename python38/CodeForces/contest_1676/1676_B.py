case = int(input())


def solve():
    n = int(input())
    boxes = [int(i) for i in input().split()]
    s = min(boxes)
    eat = [i - s for i in boxes]
    print(sum(eat))


while case:
    solve()
    case += -1
