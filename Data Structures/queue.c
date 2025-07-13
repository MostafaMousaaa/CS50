#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct queue_node
{
    int data;
    struct queue_node *next;
}
queue_node;

typedef struct
{
    queue_node *front;
    queue_node *rear;
    int size;
}
queue;

queue *create_queue(void);
bool enqueue(queue *q, int value);
bool dequeue(queue *q, int *value);
bool front_queue(queue *q, int *value);
bool is_queue_empty(queue *q);
int queue_size(queue *q);
void print_queue(queue *q);
void free_queue(queue *q);

int main(void)
{
    printf("=== Queue Demo (FIFO) ===\n");
    queue *q = create_queue();
    
    if (q == NULL)
    {
        printf("Failed to create queue\n");
        return 1;
    }
    
    // Enqueue elements
    printf("Enqueuing elements: 10, 20, 30, 40\n");
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    enqueue(q, 40);
    
    printf("Queue contents (front to rear):\n");
    print_queue(q);
    printf("Queue size: %d\n", queue_size(q));
    
    // Check front element
    int front_value;
    if (front_queue(q, &front_value))
    {
        printf("Front element: %d\n", front_value);
    }
    
    // Dequeue elements
    printf("\nDequeuing elements:\n");
    int dequeued_value;
    while (!is_queue_empty(q))
    {
        if (dequeue(q, &dequeued_value))
        {
            printf("Dequeued: %d\n", dequeued_value);
        }
    }
    
    printf("Queue is now empty: %s\n", is_queue_empty(q) ? "Yes" : "No");
    
    free_queue(q);
    return 0;
}

queue *create_queue(void)
{
    queue *q = malloc(sizeof(queue));
    if (q != NULL)
    {
        q->front = NULL;
        q->rear = NULL;
        q->size = 0;
    }
    return q;
}

bool enqueue(queue *q, int value)
{
    if (q == NULL)
        return false;
    
    queue_node *new_node = malloc(sizeof(queue_node));
    if (new_node == NULL)
        return false;
    
    new_node->data = value;
    new_node->next = NULL;
    
    if (q->rear == NULL)
    {
        // Queue is empty
        q->front = q->rear = new_node;
    }
    else
    {
        // Add to rear
        q->rear->next = new_node;
        q->rear = new_node;
    }
    
    q->size++;
    return true;
}

bool dequeue(queue *q, int *value)
{
    if (q == NULL || q->front == NULL)
        return false;
    
    queue_node *temp = q->front;
    *value = temp->data;
    
    q->front = q->front->next;
    
    // If queue becomes empty
    if (q->front == NULL)
    {
        q->rear = NULL;
    }
    
    q->size--;
    free(temp);
    return true;
}

bool front_queue(queue *q, int *value)
{
    if (q == NULL || q->front == NULL)
        return false;
    
    *value = q->front->data;
    return true;
}

bool is_queue_empty(queue *q)
{
    return (q == NULL || q->front == NULL);
}

int queue_size(queue *q)
{
    return (q != NULL) ? q->size : 0;
}

void print_queue(queue *q)
{
    if (q == NULL || q->front == NULL)
    {
        printf("Queue is empty\n");
        return;
    }
    
    queue_node *current = q->front;
    while (current != NULL)
    {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void free_queue(queue *q)
{
    if (q == NULL)
        return;
    
    queue_node *current = q->front;
    while (current != NULL)
    {
        queue_node *next = current->next;
        free(current);
        current = next;
    }
    
    free(q);
}
