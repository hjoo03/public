#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <malloc.h>


typedef char* string;

int main() {
	string st = "hello, world!";
	printf("%s", st);

	return 0;
}
