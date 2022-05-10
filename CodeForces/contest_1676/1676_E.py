from bisect import bisect_left

case = int(input())


def solve():
    n, q = map(int, input().split())
    candies = [int(i) for i in input().split()]
    candies.sort()
    candies.reverse()

    for i in range(1, n):
        candies[i] += candies[i - 1]

    for i in range(0, q):
        goal = int(input())
        if candies[-1] < goal:
            print(-1)
        else:
            print(bisect_left(candies, goal) + 1)


while case:
    solve()
    case += -1
