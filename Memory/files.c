#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Open file for writing
    FILE *file = fopen("phonebook.csv", "w");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    
    // Get input and write to file
    string name = get_string("Name: ");
    string number = get_string("Number: ");
    
    fprintf(file, "%s,%s\n", name, number);
    fclose(file);
    
    // Read from file
    file = fopen("phonebook.csv", "r");
    if (file == NULL)
    {
        printf("Could not open file for reading.\n");
        return 1;
    }
    
    printf("Contents of phonebook.csv:\n");
    char buffer[100];
    while (fgets(buffer, sizeof(buffer), file) != NULL)
    {
        printf("%s", buffer);
    }
    
    fclose(file);
    
    // Binary file example
    FILE *binary_file = fopen("numbers.bin", "wb");
    if (binary_file == NULL)
    {
        printf("Could not create binary file.\n");
        return 1;
    }
    
    int numbers[] = {1, 2, 3, 4, 5};
    fwrite(numbers, sizeof(int), 5, binary_file);
    fclose(binary_file);
    
    // Read binary file
    binary_file = fopen("numbers.bin", "rb");
    if (binary_file == NULL)
    {
        printf("Could not open binary file for reading.\n");
        return 1;
    }
    
    int read_numbers[5];
    fread(read_numbers, sizeof(int), 5, binary_file);
    fclose(binary_file);
    
    printf("Numbers from binary file: ");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", read_numbers[i]);
    }
    printf("\n");
    
    return 0;
}
