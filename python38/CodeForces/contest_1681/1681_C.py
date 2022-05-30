# from bisect import *
# from math import *
from io import BytesIO, IOBase
import os, sys
try:
	sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
	# noinspection PyUnresolvedReferences
	from debug.debug import Debug
	debug = Debug().debug
except ModuleNotFoundError:
	pass
# ----------------------------------------------------------------------------------------------------------------------


def main():  # TODO: Incomplete Solution
	case = int(input())

	def solve():
		global count
		n = int(input())
		arr1 = list(map(int, input().split()))
		arr2 = list(map(int, input().split()))

		swaps = []
		count = 0

		def swap(i1, i2):
			global count
			ta1 = arr1[i1]
			ta2 = arr1[i2]
			tb1 = arr2[i1]
			tb2 = arr2[i2]
			arr1[i1] = ta2
			arr1[i2] = ta1
			arr2[i1] = tb2
			arr2[i2] = tb1
			swaps.append((i2, i1))
			count += 1

		arr1_elements = sorted(set(arr1))
		target_index = 0
		min_index_prev = 100
		for element in arr1_elements:
			duplicated_element_count = 0
			while True:
				min_index = n - arr1[::-1].index(element) - 1  # select from right to left
				if target_index == min_index:
					target_index += 1
					break
				elif target_index > min_index:
					break
				if duplicated_element_count != 0:
					if min_index == min_index_prev:
						break

				if arr2[target_index] < arr2[min_index]:
					print(-1)
					return
				else:
					swap(target_index, min_index)
					if count > 10000:
						print(-1)
						return
					min_index_prev = target_index
					target_index += 1

				duplicated_element_count += 1

			prev = 101
			same = []
			same_sub = []
			for i in range(len(arr1)):
				if arr1[i] == prev:
					same_sub.append(i)
				else:
					if len(same_sub) > 2:
						same.append(same_sub)
				prev = i
				same_sub = [i]

			for sames in same:
				pass

		print(len(swaps))
		for s1, s2 in swaps:
			print(s1 + 1, s2 + 1)
		return

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
