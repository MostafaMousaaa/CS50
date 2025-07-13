#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = get_string("Name: ");
    
    // Print string length
    printf("Length: %lu\n", strlen(name));
    
    // Print each character
    printf("Characters:\n");
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        printf("%c\n", name[i]);
    }
    
    // Convert to uppercase
    printf("Uppercase: ");
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        printf("%c", toupper(name[i]));
    }
    printf("\n");
    
    // Count vowels
    int vowels = 0;
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        char c = tolower(name[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        {
            vowels++;
        }
    }
    printf("Vowels: %d\n", vowels);
    
    return 0;
}
