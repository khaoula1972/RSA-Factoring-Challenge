#include <stdio.h>
#include <math.h>
#include <gmp.h>

void factorize_ulonglong(unsigned long long int number) {
    unsigned long long int sqrt_n = (unsigned long long int)sqrt(number);
    unsigned long long int i = 2;

    while (i <= sqrt_n) {
        unsigned long long int q = number / i;
        unsigned long long int r = number % i;

        if (r == 0) {
            printf("%llu=%llu*%llu\n", number, q, i);
            return;
        }

        i++;
    }

    printf("%llu=%llu*1\n", number, number);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: factors <file>\n");
        return 1;
    }

    FILE* file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("File '%s' not found.\n", argv[1]);
        return 1;
    }

    unsigned long long int number;

    while (fscanf(file, "%llu", &number) != EOF) {
        factorize_ulonglong(number);
    }

    fclose(file);
    return 0;
}
