#include <stdio.h>

main()
{
	float celsius;
	int fahr, lower, upper, step;

	lower = 0;
	upper = 300;
	step = 20;

	printf("%3c %6c\n", 'F', 'C');

	fahr = lower;
	while (fahr <= upper) {
		celsius = (5.0 / 9.0) * (fahr - 32);
		printf("%3d %6.1f\n", fahr, celsius);
		fahr = fahr + step;
	}
}
