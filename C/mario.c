#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    
    // Get height from user (1-8)
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    
    // Print pyramid
    for (int i = 0; i < n; i++)
    {
        // Print spaces
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        
        // Print hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        
        printf("\n");
    }
    
    return 0;
}
