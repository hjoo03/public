# from bisect import *
# from math import *
from collections import defaultdict
from io import BytesIO, IOBase
import os, sys

try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    # noinspection PyUnresolvedReferences
    from debug.debug import Debug

    dbg = Debug().dbg
except ModuleNotFoundError:
    pass


# ----------------------------------------------------------------------------------------------------------------------


def main():
    case = int(input())

    def solve():
        n, k = map(int, input().split())
        arr = sorted(list(map(int, input().split())))  # TODO: Why using sorted() function?

        count_dict = defaultdict(int)
        for i in arr:
            count_dict[i] += 1

        ok = []

        for key in count_dict:
            if count_dict[key] >= k:
                ok.append(key)

        if not ok: print(-1); return
        ok.sort()
        ok.append(10**18)
        ans, now, left, cnt = 0, -2, -2, 0
        for i in ok:
            if i == now + 1:
                cnt += 1
                now += 1
            else:
                if ans < cnt:
                    ans = cnt
                    ansL = left
                    ansR = now
                cnt = 1
                left, now = i, i
        print(ansL, ansR)

    while case:
        solve()
        case += -1


# ----------------------------------------------------------------------------------------------------------------------
def gcd(gcd_x, gcd_y):
    while gcd_y:
        gcd_x, gcd_y = gcd_y, gcd_x % gcd_y
    return gcd_x


def lcm(lcm_x, lcm_y):
    return lcm_x * lcm_y // gcd(lcm_x, lcm_y)


def isprime(integer_x):
    if integer_x <= 1:
        return False
    for i in range(2, int(integer_x ** 0.5) + 1):
        if integer_x % i == 0:
            return False
    return True


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, **kwargs):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input(): return sys.stdin.readline().rstrip('\r\n')


if __name__ == '__main__':
    main()
