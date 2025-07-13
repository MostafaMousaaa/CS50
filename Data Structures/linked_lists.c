#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

// Singly linked list node
typedef struct node
{
    int data;
    struct node *next;
}
node;

// Doubly linked list node
typedef struct dnode
{
    int data;
    struct dnode *next;
    struct dnode *prev;
}
dnode;

// Function prototypes
node *create_node(int value);
void insert_beginning(node **head, int value);
void insert_end(node **head, int value);
void delete_node(node **head, int value);
bool search(node *head, int value);
void print_list(node *head);
void free_list(node *head);

dnode *create_dnode(int value);
void insert_beginning_double(dnode **head, int value);
void print_double_list(dnode *head);
void free_double_list(dnode *head);

int main(void)
{
    printf("=== Singly Linked List Demo ===\n");
    node *list = NULL;
    
    // Insert elements
    insert_beginning(&list, 3);
    insert_beginning(&list, 2);
    insert_beginning(&list, 1);
    insert_end(&list, 4);
    insert_end(&list, 5);
    
    printf("List: ");
    print_list(list);
    
    // Search for elements
    printf("Search for 3: %s\n", search(list, 3) ? "Found" : "Not found");
    printf("Search for 6: %s\n", search(list, 6) ? "Found" : "Not found");
    
    // Delete element
    delete_node(&list, 3);
    printf("After deleting 3: ");
    print_list(list);
    
    free_list(list);
    
    printf("\n=== Doubly Linked List Demo ===\n");
    dnode *double_list = NULL;
    
    insert_beginning_double(&double_list, 10);
    insert_beginning_double(&double_list, 20);
    insert_beginning_double(&double_list, 30);
    
    printf("Double list: ");
    print_double_list(double_list);
    
    free_double_list(double_list);
    
    return 0;
}

node *create_node(int value)
{
    node *new_node = malloc(sizeof(node));
    if (new_node != NULL)
    {
        new_node->data = value;
        new_node->next = NULL;
    }
    return new_node;
}

void insert_beginning(node **head, int value)
{
    node *new_node = create_node(value);
    if (new_node != NULL)
    {
        new_node->next = *head;
        *head = new_node;
    }
}

void insert_end(node **head, int value)
{
    node *new_node = create_node(value);
    if (new_node == NULL)
        return;
    
    if (*head == NULL)
    {
        *head = new_node;
        return;
    }
    
    node *current = *head;
    while (current->next != NULL)
    {
        current = current->next;
    }
    current->next = new_node;
}

void delete_node(node **head, int value)
{
    if (*head == NULL)
        return;
    
    if ((*head)->data == value)
    {
        node *temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    
    node *current = *head;
    while (current->next != NULL && current->next->data != value)
    {
        current = current->next;
    }
    
    if (current->next != NULL)
    {
        node *temp = current->next;
        current->next = current->next->next;
        free(temp);
    }
}

bool search(node *head, int value)
{
    node *current = head;
    while (current != NULL)
    {
        if (current->data == value)
            return true;
        current = current->next;
    }
    return false;
}

void print_list(node *head)
{
    node *current = head;
    while (current != NULL)
    {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

void free_list(node *head)
{
    node *current = head;
    while (current != NULL)
    {
        node *next = current->next;
        free(current);
        current = next;
    }
}

dnode *create_dnode(int value)
{
    dnode *new_node = malloc(sizeof(dnode));
    if (new_node != NULL)
    {
        new_node->data = value;
        new_node->next = NULL;
        new_node->prev = NULL;
    }
    return new_node;
}

void insert_beginning_double(dnode **head, int value)
{
    dnode *new_node = create_dnode(value);
    if (new_node != NULL)
    {
        new_node->next = *head;
        if (*head != NULL)
            (*head)->prev = new_node;
        *head = new_node;
    }
}

void print_double_list(dnode *head)
{
    dnode *current = head;
    while (current != NULL)
    {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

void free_double_list(dnode *head)
{
    dnode *current = head;
    while (current != NULL)
    {
        dnode *next = current->next;
        free(current);
        current = next;
    }
}
