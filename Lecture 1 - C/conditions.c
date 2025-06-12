#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");
    
    // Simple if-else
    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
    
    // Logical operators
    if (x > 0 && y > 0)
    {
        printf("Both numbers are positive\n");
    }
    
    if (x < 0 || y < 0)
    {
        printf("At least one number is negative\n");
    }
    
    return 0;
}
