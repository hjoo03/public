case = int(input())


def solve(number_log, log_list):
    total = sum(log_list) - number_log
    print("errorgorn") if total % 2 == 1 else print("maomao90")


while case:
    log = int(input())
    logs = input().split()
    logs = [int(i) for i in logs]
    solve(log, logs)
    case += -1