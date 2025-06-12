#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    int capacity = 2;
    int size = 0;
    
    // Allocate memory for phonebook
    person *phonebook = malloc(capacity * sizeof(person));
    if (phonebook == NULL)
    {
        return 1;
    }
    
    // Add people to phonebook
    while (true)
    {
        string name = get_string("Name (or 'quit' to stop): ");
        if (strcmp(name, "quit") == 0)
        {
            break;
        }
        
        string number = get_string("Number: ");
        
        // Check if we need more space
        if (size >= capacity)
        {
            capacity *= 2;
            person *temp = realloc(phonebook, capacity * sizeof(person));
            if (temp == NULL)
            {
                free(phonebook);
                return 1;
            }
            phonebook = temp;
            printf("Expanded phonebook capacity to %i\n", capacity);
        }
        
        // Allocate memory for strings
        phonebook[size].name = malloc(strlen(name) + 1);
        phonebook[size].number = malloc(strlen(number) + 1);
        
        if (phonebook[size].name == NULL || phonebook[size].number == NULL)
        {
            // Clean up and exit
            for (int i = 0; i < size; i++)
            {
                free(phonebook[i].name);
                free(phonebook[i].number);
            }
            free(phonebook);
            return 1;
        }
        
        strcpy(phonebook[size].name, name);
        strcpy(phonebook[size].number, number);
        size++;
    }
    
    // Print phonebook
    printf("\nPhonebook:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%s: %s\n", phonebook[i].name, phonebook[i].number);
    }
    
    // Free all allocated memory
    for (int i = 0; i < size; i++)
    {
        free(phonebook[i].name);
        free(phonebook[i].number);
    }
    free(phonebook);
    
    return 0;
}
