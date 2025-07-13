#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("n = %i\n", n);
    printf("Address of n: %p\n", &n);
    
    // Pointer to n
    int *p = &n;
    printf("p = %p\n", p);
    printf("Value at p: %i\n", *p);
    
    // Change value through pointer
    *p = 100;
    printf("After *p = 100:\n");
    printf("n = %i\n", n);
    printf("*p = %i\n", *p);
    
    // String example
    string s = "HI!";
    printf("\nString s = %s\n", s);
    printf("Address of s: %p\n", s);
    
    // Print each character and its address
    for (int i = 0; s[i] != '\0'; i++)
    {
        printf("s[%i] = %c, address: %p\n", i, s[i], &s[i]);
    }
    
    // Pointer arithmetic
    char *ptr = s;
    printf("\nPointer arithmetic:\n");
    printf("*ptr = %c\n", *ptr);
    printf("*(ptr + 1) = %c\n", *(ptr + 1));
    printf("*(ptr + 2) = %c\n", *(ptr + 2));
    
    return 0;
}
