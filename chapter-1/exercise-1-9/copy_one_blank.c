#include <stdio.h>

main()
{
	unsigned skip;
	int c;

	skip = 0;
	while ((c = getchar()) != EOF) {
		if (c == ' ') {
			skip = 1;
		} else {
			if (skip) {
				putchar(' ');
				skip = 0;
			}
			putchar(c);
		}
	}
}
