#include <stdio.h>

main()
{
	int x, y;
	x = getchar() != EOF;
	y = getchar() != EOF;
	printf("%d\n", x);
	printf("%d\n", y);
}
