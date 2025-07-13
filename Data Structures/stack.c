#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct stack_node
{
    int data;
    struct stack_node *next;
}
stack_node;

typedef struct
{
    stack_node *top;
    int size;
}
stack;

stack *create_stack(void);
bool push(stack *s, int value);
bool pop(stack *s, int *value);
bool peek(stack *s, int *value);
bool is_empty(stack *s);
int stack_size(stack *s);
void print_stack(stack *s);
void free_stack(stack *s);

int main(void)
{
    printf("=== Stack Demo (LIFO) ===\n");
    stack *s = create_stack();
    
    if (s == NULL)
    {
        printf("Failed to create stack\n");
        return 1;
    }
    
    // Push elements
    printf("Pushing elements: 10, 20, 30, 40\n");
    push(s, 10);
    push(s, 20);
    push(s, 30);
    push(s, 40);
    
    printf("Stack contents (top to bottom):\n");
    print_stack(s);
    printf("Stack size: %d\n", stack_size(s));
    
    // Peek at top
    int top_value;
    if (peek(s, &top_value))
    {
        printf("Top element: %d\n", top_value);
    }
    
    // Pop elements
    printf("\nPopping elements:\n");
    int popped_value;
    while (!is_empty(s))
    {
        if (pop(s, &popped_value))
        {
            printf("Popped: %d\n", popped_value);
        }
    }
    
    printf("Stack is now empty: %s\n", is_empty(s) ? "Yes" : "No");
    
    free_stack(s);
    return 0;
}

stack *create_stack(void)
{
    stack *s = malloc(sizeof(stack));
    if (s != NULL)
    {
        s->top = NULL;
        s->size = 0;
    }
    return s;
}

bool push(stack *s, int value)
{
    if (s == NULL)
        return false;
    
    stack_node *new_node = malloc(sizeof(stack_node));
    if (new_node == NULL)
        return false;
    
    new_node->data = value;
    new_node->next = s->top;
    s->top = new_node;
    s->size++;
    
    return true;
}

bool pop(stack *s, int *value)
{
    if (s == NULL || s->top == NULL)
        return false;
    
    stack_node *temp = s->top;
    *value = temp->data;
    s->top = s->top->next;
    s->size--;
    
    free(temp);
    return true;
}

bool peek(stack *s, int *value)
{
    if (s == NULL || s->top == NULL)
        return false;
    
    *value = s->top->data;
    return true;
}

bool is_empty(stack *s)
{
    return (s == NULL || s->top == NULL);
}

int stack_size(stack *s)
{
    return (s != NULL) ? s->size : 0;
}

void print_stack(stack *s)
{
    if (s == NULL || s->top == NULL)
    {
        printf("Stack is empty\n");
        return;
    }
    
    stack_node *current = s->top;
    while (current != NULL)
    {
        printf("%d\n", current->data);
        current = current->next;
    }
}

void free_stack(stack *s)
{
    if (s == NULL)
        return;
    
    stack_node *current = s->top;
    while (current != NULL)
    {
        stack_node *next = current->next;
        free(current);
        current = next;
    }
    
    free(s);
}
