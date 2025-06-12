#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

node *create_node(int value);
void print_list(node *head);
void free_list(node *head);

int main(void)
{
    node *list = NULL;
    
    // Add numbers to list
    for (int i = 0; i < 3; i++)
    {
        int number = get_int("Number: ");
        
        node *n = create_node(number);
        if (n == NULL)
        {
            printf("Memory allocation failed\n");
            free_list(list);
            return 1;
        }
        
        // Add to beginning of list
        n->next = list;
        list = n;
    }
    
    // Print list
    printf("Your list: ");
    print_list(list);
    
    // Show memory addresses
    printf("\nMemory addresses:\n");
    node *ptr = list;
    int i = 0;
    while (ptr != NULL)
    {
        printf("Node %d: address = %p, value = %d, next = %p\n", 
               i, ptr, ptr->number, ptr->next);
        ptr = ptr->next;
        i++;
    }
    
    // Free memory
    free_list(list);
    
    return 0;
}

node *create_node(int value)
{
    node *n = malloc(sizeof(node));
    if (n != NULL)
    {
        n->number = value;
        n->next = NULL;
    }
    return n;
}

void print_list(node *head)
{
    node *ptr = head;
    while (ptr != NULL)
    {
        printf("%d ", ptr->number);
        ptr = ptr->next;
    }
    printf("\n");
}

void free_list(node *head)
{
    node *ptr = head;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}
