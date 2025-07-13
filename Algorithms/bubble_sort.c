#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

void bubble_sort(int arr[], int n);
void print_array(int arr[], int n);
void swap(int *a, int *b);

int main(void)
{
    int numbers[] = {64, 34, 25, 12, 22, 11, 90};
    int size = 7;
    
    printf("Original array: ");
    print_array(numbers, size);
    
    bubble_sort(numbers, size);
    
    printf("Sorted array: ");
    print_array(numbers, size);
    
    return 0;
}

void bubble_sort(int arr[], int n)
{
    printf("\nBubble Sort Process:\n");
    
    for (int i = 0; i < n - 1; i++)
    {
        bool swapped = false;
        
        // Last i elements are already sorted
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        
        printf("After pass %d: ", i + 1);
        print_array(arr, n);
        
        // If no swapping occurred, array is sorted
        if (!swapped)
        {
            printf("Array is now sorted!\n");
            break;
        }
    }
}

void print_array(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
