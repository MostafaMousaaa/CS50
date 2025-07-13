#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get input from user
    int x = get_int("x: ");
    int y = get_int("y: ");
    
    // Perform calculations
    printf("x + y = %i\n", x + y);
    printf("x - y = %i\n", x - y);
    printf("x * y = %i\n", x * y);
    printf("x / y = %i\n", x / y);
    printf("x %% y = %i\n", x % y);
    
    return 0;
}
