#include <stdio.h>

main()
{
	float fahr;
	int celsius, lower, upper, step;

	lower = 0;
	upper = 300;
	step = 20;

	printf("%3c %6c\n", 'C', 'F');

	celsius = lower;
	while (celsius <= upper) {
		fahr = (9.0 / 5.0) * celsius + 32;
		printf("%3d %6.1f\n", celsius, fahr);
		celsius += step;
	}
}
