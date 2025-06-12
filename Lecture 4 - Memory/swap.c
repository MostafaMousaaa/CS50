#include <cs50.h>
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");
    
    printf("Before swap: x = %i, y = %i\n", x, y);
    printf("Addresses: &x = %p, &y = %p\n", &x, &y);
    
    swap(&x, &y);
    
    printf("After swap: x = %i, y = %i\n", x, y);
    
    return 0;
}

void swap(int *a, int *b)
{
    printf("In swap function:\n");
    printf("Address a points to: %p\n", a);
    printf("Address b points to: %p\n", b);
    printf("Values: *a = %i, *b = %i\n", *a, *b);
    
    int temp = *a;
    *a = *b;
    *b = temp;
    
    printf("After swapping: *a = %i, *b = %i\n", *a, *b);
}
