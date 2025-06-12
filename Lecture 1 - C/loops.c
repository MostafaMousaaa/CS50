#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    // While loop
    printf("While loop:\n");
    int i = 0;
    while (i < 3)
    {
        printf("meow\n");
        i++;
    }
    
    // For loop
    printf("\nFor loop:\n");
    for (int j = 0; j < 3; j++)
    {
        printf("meow\n");
    }
    
    // Do-while loop
    printf("\nDo-while loop (get positive number):\n");
    int n;
    do
    {
        n = get_int("Positive number: ");
    }
    while (n < 1);
    
    // Use function
    printf("\nUsing function:\n");
    meow(n);
    
    return 0;
}

// Function to print meow n times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
