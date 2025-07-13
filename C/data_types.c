#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Integer types
    int age = 25;
    long population = 8000000000;
    
    // Floating point types
    float price = 3.99;
    double pi = 3.14159265359;
    
    // Character and string
    char grade = 'A';
    string name = "Alice";
    
    // Boolean (requires stdbool.h for true/false keywords)
    bool is_student = true;
    
    // Print different data types
    printf("Age: %d\n", age);
    printf("Population: %ld\n", population);
    printf("Price: %.2f\n", price);
    printf("Pi: %.10f\n", pi);
    printf("Grade: %c\n", grade);
    printf("Name: %s\n", name);
    printf("Is student: %d\n", is_student);
    
    return 0;
}
