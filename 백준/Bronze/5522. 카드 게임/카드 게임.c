#include <stdio.h>

int main(void) {
	int res = 0, t;

	for (int i = 0; i < 5; i++) {
		scanf("%d", &t);
		res += t;
	}

	printf("%d", res);
	return 0;
}