#include <stdio.h>

main()
{
	unsigned blank_count, tab_count, newline_count;
	int c;

	blank_count = 0;
	tab_count = 0;
	newline_count = 0;

	while ((c = getchar()) != EOF) {
		if (c == ' ') {
			++blank_count;
		} else if (c == '\t') {
			++tab_count;
		} else if (c == '\n') {
			++newline_count;
		}
	}

	printf("Blanks: %u\n", blank_count);
	printf("Tabs: %u\n", tab_count);
	printf("Newlines: %u\n", newline_count);
}
