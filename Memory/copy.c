#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get input
    string s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }
    
    // Allocate memory for copy
    string t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }
    
    // Copy string manually
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }
    
    // Or use strcpy
    // strcpy(t, s);
    
    // Capitalize first letter of copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }
    
    printf("s: %s\n", s);
    printf("t: %s\n", t);
    
    // Show addresses
    printf("Address of s: %p\n", s);
    printf("Address of t: %p\n", t);
    
    // Free allocated memory
    free(t);
    
    return 0;
}
