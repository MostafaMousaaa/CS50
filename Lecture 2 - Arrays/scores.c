#include <cs50.h>
#include <stdio.h>

const int TOTAL = 3;

float average(int length, int array[]);

int main(void)
{
    int scores[TOTAL];
    
    // Get scores from user
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Score %d: ", i + 1);
    }
    
    // Calculate and print average
    printf("Average: %.1f\n", average(TOTAL, scores));
    
    return 0;
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
