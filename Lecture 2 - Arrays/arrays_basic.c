#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Declare and initialize array
    int scores[3];
    scores[0] = get_int("Score 1: ");
    scores[1] = get_int("Score 2: ");
    scores[2] = get_int("Score 3: ");
    
    // Calculate and print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    
    // Array with initial values
    int numbers[] = {4, 6, 8, 2, 7, 5, 0};
    int length = 7;
    
    // Find maximum
    int max = numbers[0];
    for (int i = 1; i < length; i++)
    {
        if (numbers[i] > max)
        {
            max = numbers[i];
        }
    }
    printf("Maximum: %d\n", max);
    
    // Print all elements
    printf("Numbers: ");
    for (int i = 0; i < length; i++)
    {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    return 0;
}
