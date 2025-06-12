#include <cs50.h>
#include <stdio.h>

void selection_sort(int arr[], int n);
void print_array(int arr[], int n);
void swap(int *a, int *b);

int main(void)
{
    int numbers[] = {64, 25, 12, 22, 11};
    int size = 5;
    
    printf("Original array: ");
    print_array(numbers, size);
    
    selection_sort(numbers, size);
    
    printf("Sorted array: ");
    print_array(numbers, size);
    
    return 0;
}

void selection_sort(int arr[], int n)
{
    printf("\nSelection Sort Process:\n");
    
    for (int i = 0; i < n - 1; i++)
    {
        int min_idx = i;
        
        // Find minimum element in remaining array
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
            {
                min_idx = j;
            }
        }
        
        // Swap minimum element with first element
        if (min_idx != i)
        {
            swap(&arr[min_idx], &arr[i]);
        }
        
        printf("After step %d: ", i + 1);
        print_array(arr, n);
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
