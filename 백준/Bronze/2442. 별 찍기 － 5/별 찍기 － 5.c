#include <stdio.h>

int main(void) {
	int start = 0;
	scanf("%d", &start);
	int star = 1;

	for (int i = 0; i < start; i++) {
		for (int j = 0; j < start-1-i; j++)
			printf(" ");
		for (int j = 0; j < star; j++)
			printf("*");
		star = star + 2;
		printf("\n");
	}
}