#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define ll long long

/* p317 #12 */

int main() {
	int end;
	printf("몇 번째 항까지 구할까요? ");
	scanf("%d", &end);

	unsigned ll next, a = 0, b = 1;

	for (int i = 0; i <= end; i++)
	{
		if (i == 0) {
			printf("%lld, ", a);
		}
		else if (i == 1) {
			printf("%lld, ", b);
		}
		else {
			next = a + b;
			if (i == end) {
				printf("%lld", next);
			}
			else {
				printf("%lld, ", next);
			}
			a = b;
			b = next;
		}
	}

	return 0;
}
