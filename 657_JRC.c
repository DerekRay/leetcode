#include "apue.h"
#include <stdbool.h>
#define true 1
#define false 0
bool judgeCircle(char* moves) {
    int x = 0;
    int y = 0;
    char *i = moves;
    for (; *i != '\0'; i++)
    {
        switch(*i)
        {
            case 'U':
                y++;
                break;
            case 'D':
                y--;
                break;
            case 'L':
                x++;
                break;
            case 'R':
                x--;
                break;
            default:
                break;    
        }    
    }        
    printf("%d,%d\n", x, y);
    return x == 0 && y ==0;
}
int main(void)
{
    char str[] = "UD";
    if (judgeCircle(str) == true)
        printf("True\n");
    else
        printf("False\n");
    return 0;
}
