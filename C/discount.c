#include <cs50.h>
#include <stdio.h>

// Function prototype
float discount(float price, int percentage);

int main(void)
{
    float regular = get_float("Regular price: ");
    int percent_off = get_int("Percent off: ");
    float sale = discount(regular, percent_off);
    printf("Sale price: %.2f\n", sale);
    return 0;
}

// Function definition
float discount(float price, int percentage)
{
    return price * (100 - percentage) / 100;
}
