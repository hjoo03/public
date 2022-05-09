inp = input().split()
case = int(inp[0])
inp.remove(str(case))


def solve(number_log, log_list):
    total = sum(log_list) - number_log
    print("errorgorn") if total % 2 == 1 else print("maomao90")


while case:
    log = int(inp[0])
    logs = [int(inp[i]) for i in range(1, log+1)]
    solve(log, logs)
    inp = inp[log+1:]
    case -= 1
