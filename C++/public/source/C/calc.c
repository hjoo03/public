#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

/* p316 #06 */

int a, b;
void add(x, y), sub(x, y), mul(x, y), div(x, y), calc(i);

int main() {
	printf("*****************\nA---- Add\nS---- Subtract\n");
	printf("M---- Multiply\nD---- Divide\nQ---- Quit\n");
	printf("*****************\n");

	do {
		printf("연산을 선택하시오: ");
		char inp;
		scanf(" %c", &inp);

		switch ((int)inp) { // convert to ascii
		case 65:
		case 97:
			calc(0); // add
			break;
		case 83:
		case 115:
			calc(1); // subtract
			break;
		case 77:
		case 109:
			calc(2); // multiply
			break;
		case 68:
		case 100:
			calc(3); // divide
			break;
		case 81:
		case 113:
			return 0; // quit
		}

	} while (1);

	return 0;
}

void calc(i) {
	printf("두수를 공백으로 분리하여 입력하시오: ");
	scanf("%d %d", &a, &b);

	switch (i) {
	case 0:
		add(a, b);
		break;
	case 1:
		sub(a, b);
		break;
	case 2:
		mul(a, b);
		break;
	case 3:
		div(a, b);
		break;
	}
}
void add(x, y) {
	printf("%d\n", x + y);
}
void sub(x, y) {
	printf("%d\n", x - y);
}
void mul(x, y) {
	printf("%d\n", x * y);
}
void div(x, y) {
	printf("%d\n", x / y);
}
