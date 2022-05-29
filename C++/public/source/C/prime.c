#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

/* p316 #07 */

typedef enum { False, True } bool;

int main() {
	int m;
	printf("최댓값을 입력하세요: ");
	scanf("%d", &m);

	for (int i = 1; i < m; i++)
	{
		bool isprime = True;

		for (int j = 2; j <= i; j++)
		{
			if (i % j == 0) {
				isprime = False;
				break;
			}
		}
		if (isprime) {
			printf("%d ", i);
		}
	}

	return 0;
}
