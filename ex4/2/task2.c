#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

// Very naive algorithm, and can easily break by adding lots of '<', '>' or '&' in input-string
const char *replace (char *str) {

    char *str_replaced;
    size_t len = strlen(str);
    str_replaced = malloc(len + 100);
    int j = 0;
    int i;

    for (i = 0; str[i] != '\0'; i++) {

        char c = str[i];
        switch(c)
        {
        case '<':
            str_replaced[j] = '&';
            str_replaced[j+1] = 'l';
            str_replaced[j+2] = 't';
            j += 3;
            break;
        case '>':
            str_replaced[j] = '&';
            str_replaced[j+1] = 'g';
            str_replaced[j+2] = 't';
            j += 3;
            break;
        case '&':
            str_replaced[j] = '&';
            str_replaced[j+1] = 'a';
            str_replaced[j+2] = 'm';
            str_replaced[j+3] = 'p';
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

int main() {
    char test1[50] = "foo <&> bar";
    char test2[50] = "<<<<<<&&&&&>>>>>>>";
    char test3[50] = "Cakes & cookies";
    char test4[50] = "C > all other languages";
    
    printf("%s \n", replace(test1));
    printf("%s \n", replace(test2));
    printf("%s \n", replace(test3));
    printf("%s \n", replace(test4));

    return 0;
}
