#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    printf("Number of arguments: %d\n", argc);
    
    // Print each argument
    for (int i = 0; i < argc; i++)
    {
        printf("argv[%d]: %s\n", i, argv[i]);
    }
    
    // Check if specific argument provided
    if (argc > 1)
    {
        printf("Hello, %s!\n", argv[1]);
    }
    else
    {
        printf("Hello, world!\n");
    }
    
    return 0;
}
