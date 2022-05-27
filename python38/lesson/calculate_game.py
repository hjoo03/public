import random
from datetime import datetime

score = 0


def main():
	global score
	operands = ['+', '*', '/', '-']

	op = operands[random.randrange(0, 4)]

	if op == '+':
		x, y = random.randrange(1, 101), random.randrange(1, 101)
		answer = x + y
	elif op == '*':
		x, y = random.randrange(1, 21), random.randrange(2, 21)
		answer = x * y
	elif op == '/':
		while True:
			x, y = random.randrange(1, 201), random.randrange(2, 11)
			if x % y == 0:
				break
		answer = x / y
	else:
		while True:
			x, y = random.randrange(1, 201), random.randrange(1, 201)
			if x >= y:
				break
		answer = x - y

	print(f"{x} {op} {y} = ?")
	while True:
		if int(input()) == answer:
			print("Correct!")
			score += 10
			return
		else:
			score -= 5
			print("Wrong!")


start = datetime.now()
for i in range(20):
	main()
elapsed_time = datetime.now() - start
if elapsed_time.seconds > 60:
	et = elapsed_time.seconds - 60
	penalty = int(et)
	score -= penalty

print(f"Score: {score}")
