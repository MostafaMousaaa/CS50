#include <cs50.h>
#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input);
void safe_function(char *input);

int main(void)
{
    printf("Buffer Overflow Demonstration\n");
    printf("=============================\n");
    
    // Safe example
    char safe_input[] = "Hello";
    printf("Safe input: %s\n", safe_input);
    safe_function(safe_input);
    
    // Warning: The following would be dangerous in real programs
    printf("\nThis program demonstrates buffer overflow concepts\n");
    printf("In real programs, always use safe string functions!\n");
    
    // Show memory layout
    int x = 42;
    int y = 24;
    char buffer[10];
    
    printf("\nMemory layout:\n");
    printf("Address of x: %p\n", &x);
    printf("Address of y: %p\n", &y);
    printf("Address of buffer: %p\n", buffer);
    
    // Safe string copy
    strncpy(buffer, "Safe", sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
    
    printf("Buffer contents: %s\n", buffer);
    printf("x = %d, y = %d\n", x, y);
    
    return 0;
}

void vulnerable_function(char *input)
{
    char buffer[10];
    // DON'T DO THIS - strcpy is dangerous!
    // strcpy(buffer, input);
    
    // Use safe alternative
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
    
    printf("Buffer: %s\n", buffer);
}

void safe_function(char *input)
{
    char buffer[50];
    size_t input_len = strlen(input);
    
    if (input_len < sizeof(buffer))
    {
        strcpy(buffer, input);
        printf("Safely copied: %s\n", buffer);
    }
    else
    {
        printf("Input too long for buffer\n");
    }
}
