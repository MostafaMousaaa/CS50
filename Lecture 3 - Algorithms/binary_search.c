#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool binary_search_int(int arr[], int n, int target);
bool binary_search_string(string arr[], int n, string target);

int main(void)
{
    // Sorted integer array (required for binary search)
    int numbers[] = {1, 5, 10, 20, 50, 100, 500};
    int size = 7;
    
    int target = get_int("Number to search for: ");
    
    if (binary_search_int(numbers, size, target))
    {
        printf("Found %d!\n", target);
    }
    else
    {
        printf("%d not found.\n", target);
    }
    
    // Sorted string array
    string names[] = {"Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"};
    int name_count = 7;
    
    string name = get_string("Name to search for: ");
    
    if (binary_search_string(names, name_count, name))
    {
        printf("Found %s!\n", name);
    }
    else
    {
        printf("%s not found.\n", name);
    }
    
    return 0;
}

bool binary_search_int(int arr[], int n, int target)
{
    int left = 0;
    int right = n - 1;
    
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
        {
            return true;
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    
    return false;
}

bool binary_search_string(string arr[], int n, string target)
{
    int left = 0;
    int right = n - 1;
    
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        int cmp = strcmp(arr[mid], target);
        
        if (cmp == 0)
        {
            return true;
        }
        else if (cmp < 0)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    
    return false;
}
