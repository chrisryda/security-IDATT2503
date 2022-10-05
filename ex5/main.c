#include "utility.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char test1[50] = "foo <&> bar";
	char test2[50] = "<<<<<<&&&&&>>>>>>>";
	char test3[50] = "Cakes & cookies";
	char test4[50] = "C > all other languages";

	printf("%s\n", replace(test1));
	printf("%s\n", replace(test2));
	printf("%s\n", replace(test3));
	printf("%s\n", replace(test4));

	return 0;
}
