# from bisect import *
from io import BytesIO, IOBase
import os, sys
try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    # noinspection PyUnresolvedReferences
    from debug.debug import Debug  # Input "@@" to create breakpoints
    dbg = Debug().dbg
except ModuleNotFoundError:
    pass
# ----------------------------------------------------------------------------------------------------------------------


def main():
    case = int(input())

    def solve():
        ans = input()
        thief = 0
        last_1 = len(ans)-1-ans[::-1].index('1') if '1' in ans else 0
        for i in range(last_1, len(ans)):
            if ans[i] == '?':
                thief += 1
            elif ans[i] == '0':
                thief += 1
                break
            else:
                thief += 1
                continue
        print(thief)

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
