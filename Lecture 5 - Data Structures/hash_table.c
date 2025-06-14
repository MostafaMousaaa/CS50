#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define HASH_SIZE 26

typedef struct hash_node
{
    char *word;
    struct hash_node *next;
}
hash_node;

typedef struct
{
    hash_node *buckets[HASH_SIZE];
}
hash_table;

unsigned int hash_function(const char *word);
hash_table *create_hash_table(void);
bool insert_hash(hash_table *table, const char *word);
bool search_hash(hash_table *table, const char *word);
void print_hash_table(hash_table *table);
void free_hash_table(hash_table *table);

int main(void)
{
    printf("=== Hash Table Demo ===\n");
    hash_table *table = create_hash_table();
    
    if (table == NULL)
    {
        printf("Failed to create hash table\n");
        return 1;
    }
    
    // Insert words
    const char *words[] = {"apple", "banana", "cherry", "date", "elderberry", 
                          "fig", "grape", "apricot", "blueberry", "cantaloupe"};
    int word_count = sizeof(words) / sizeof(words[0]);
    
    printf("Inserting words:\n");
    for (int i = 0; i < word_count; i++)
    {
        printf("Inserting '%s' (hash: %u)\n", words[i], hash_function(words[i]));
        insert_hash(table, words[i]);
    }
    
    printf("\nHash table contents:\n");
    print_hash_table(table);
    
    // Search for words
    printf("\nSearching:\n");
    printf("Search for 'apple': %s\n", search_hash(table, "apple") ? "Found" : "Not found");
    printf("Search for 'orange': %s\n", search_hash(table, "orange") ? "Found" : "Not found");
    printf("Search for 'grape': %s\n", search_hash(table, "grape") ? "Found" : "Not found");
    
    free_hash_table(table);
    return 0;
}

unsigned int hash_function(const char *word)
{
    // Simple hash: first letter of word
    return toupper(word[0]) - 'A';
}

hash_table *create_hash_table(void)
{
    hash_table *table = malloc(sizeof(hash_table));
    if (table != NULL)
    {
        for (int i = 0; i < HASH_SIZE; i++)
        {
            table->buckets[i] = NULL;
        }
    }
    return table;
}

bool insert_hash(hash_table *table, const char *word)
{
    if (table == NULL || word == NULL)
        return false;
    
    unsigned int index = hash_function(word);
    
    // Create new node
    hash_node *new_node = malloc(sizeof(hash_node));
    if (new_node == NULL)
        return false;
    
    new_node->word = malloc(strlen(word) + 1);
    if (new_node->word == NULL)
    {
        free(new_node);
        return false;
    }
    
    strcpy(new_node->word, word);
    
    // Insert at beginning of chain
    new_node->next = table->buckets[index];
    table->buckets[index] = new_node;
    
    return true;
}

bool search_hash(hash_table *table, const char *word)
{
    if (table == NULL || word == NULL)
        return false;
    
    unsigned int index = hash_function(word);
    hash_node *current = table->buckets[index];
    
    while (current != NULL)
    {
        if (strcmp(current->word, word) == 0)
            return true;
        current = current->next;
    }
    
    return false;
}

void print_hash_table(hash_table *table)
{
    if (table == NULL)
        return;
    
    for (int i = 0; i < HASH_SIZE; i++)
    {
        printf("Bucket %d (%c): ", i, 'A' + i);
        hash_node *current = table->buckets[i];
        
        if (current == NULL)
        {
            printf("empty\n");
        }
        else
        {
            while (current != NULL)
            {
                printf("%s", current->word);
                if (current->next != NULL)
                    printf(" -> ");
                current = current->next;
            }
            printf("\n");
        }
    }
}

void free_hash_table(hash_table *table)
{
    if (table == NULL)
        return;
    
    for (int i = 0; i < HASH_SIZE; i++)
    {
        hash_node *current = table->buckets[i];
        while (current != NULL)
        {
            hash_node *next = current->next;
            free(current->word);
            free(current);
            current = next;
        }
    }
    
    free(table);
}
