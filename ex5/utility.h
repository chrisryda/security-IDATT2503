#pragma once
#include <stdlib.h>
#include <string.h>

size_t get_length_of_new_string(char *str)
{
	size_t len = strlen(str);

	for (int i = 0; str[i] != '\0'; i++)
	{

		char c = str[i];
		switch (c)
		{
		case '<':
			len += 2;
			break;
		case '>':
			len += 2;
			break;
		case '&':
			len += 3;
			break;
		default:
			break;
		}
	}

	return len;
}

char *replace(char *str)
{
	char *str_replaced;
	size_t len = get_length_of_new_string(str);
	str_replaced = malloc(len + 1);

	int j = 0;
	for (int i = 0; str[i] != '\0'; i++)
	{
		char c = str[i];
		switch (c)
		{
		case '<':
			str_replaced[j] = '&';
			str_replaced[j + 1] = 'l';
			str_replaced[j + 2] = 't';
			j += 3;
			break;
		case '>':
			str_replaced[j] = '&';
			str_replaced[j + 1] = 'g';
			str_replaced[j + 2] = 't';
			j += 3;
			break;
		case '&':
			str_replaced[j] = '&';
			str_replaced[j + 1] = 'a';
			str_replaced[j + 2] = 'm';
			str_replaced[j + 3] = 'p';
			j += 4;
			break;
		default:
			str_replaced[j] = c;
			j++;
			break;
		}
	}
	str_replaced[j] = '\0';

	return str_replaced;
}
