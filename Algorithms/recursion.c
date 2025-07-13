#include <cs50.h>
#include <stdio.h>

int factorial(int n);
int fibonacci(int n);
void draw_pyramid(int height);
void draw_level(int spaces, int hashes);

int main(void)
{
    // Factorial example
    int n = get_int("Calculate factorial of: ");
    printf("%d! = %d\n", n, factorial(n));
    
    // Fibonacci example
    int fib_n = get_int("Fibonacci number position: ");
    printf("Fibonacci(%d) = %d\n", fib_n, fibonacci(fib_n));
    
    // Recursive pyramid drawing
    int height = get_int("Pyramid height: ");
    draw_pyramid(height);
    
    return 0;
}

int factorial(int n)
{
    // Base case
    if (n <= 1)
    {
        return 1;
    }
    
    // Recursive case
    return n * factorial(n - 1);
}

int fibonacci(int n)
{
    // Base cases
    if (n <= 1)
    {
        return n;
    }
    
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2);
}

void draw_pyramid(int height)
{
    // Base case
    if (height <= 0)
    {
        return;
    }
    
    // Recursive case: draw upper part first
    draw_pyramid(height - 1);
    
    // Then draw current level
    draw_level(height - 1, height);
}

void draw_level(int spaces, int hashes)
{
    for (int i = 0; i < spaces; i++)
    {
        printf(" ");
    }
    for (int i = 0; i < hashes; i++)
    {
        printf("#");
    }
    printf("\n");
}
