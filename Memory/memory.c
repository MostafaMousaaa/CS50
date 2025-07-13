#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Allocate memory for an integer
    int *x = malloc(sizeof(int));
    if (x == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    *x = 42;
    printf("Value: %i, Address: %p\n", *x, x);
    free(x);
    
    // Allocate memory for array
    int n = get_int("How many integers? ");
    int *list = malloc(n * sizeof(int));
    if (list == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Fill array
    for (int i = 0; i < n; i++)
    {
        list[i] = get_int("Integer %i: ", i + 1);
    }
    
    // Print array
    printf("Your numbers: ");
    for (int i = 0; i < n; i++)
    {
        printf("%i ", list[i]);
    }
    printf("\n");
    
    // Reallocate to larger size
    int *temp = realloc(list, (n + 1) * sizeof(int));
    if (temp == NULL)
    {
        free(list);
        printf("Reallocation failed\n");
        return 1;
    }
    list = temp;
    
    // Add one more number
    list[n] = get_int("One more integer: ");
    n++;
    
    // Print expanded array
    printf("Expanded array: ");
    for (int i = 0; i < n; i++)
    {
        printf("%i ", list[i]);
    }
    printf("\n");
    
    free(list);
    return 0;
}
