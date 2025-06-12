#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool linear_search_int(int arr[], int n, int target);
bool linear_search_string(string arr[], int n, string target);

int main(void)
{
    // Integer array example
    int numbers[] = {20, 500, 10, 5, 100, 1, 50};
    int size = 7;
    
    int target = get_int("Number to search for: ");
    
    if (linear_search_int(numbers, size, target))
    {
        printf("Found %d!\n", target);
    }
    else
    {
        printf("%d not found.\n", target);
    }
    
    // String array example
    string names[] = {"Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"};
    int name_count = 7;
    
    string name = get_string("Name to search for: ");
    
    if (linear_search_string(names, name_count, name))
    {
        printf("Found %s!\n", name);
    }
    else
    {
        printf("%s not found.\n", name);
    }
    
    return 0;
}

bool linear_search_int(int arr[], int n, int target)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            return true;
        }
    }
    return false;
}

bool linear_search_string(string arr[], int n, string target)
{
    for (int i = 0; i < n; i++)
    {
        if (strcmp(arr[i], target) == 0)
        {
            return true;
        }
    }
    return false;
}
