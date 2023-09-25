#include <stdio.h>

int main(void) {
    int A, B, V, day, dayup;

    scanf("%d %d %d", &A, &B, &V);
    dayup = A - B;

    V = V - B;
    day = V / dayup;
    V = V % dayup;

    if (V == 0) {
        printf("%d", day);
    }
    else {
        printf("%d", (day + 1));
    }

    return 0;
}