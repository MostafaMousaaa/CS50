#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

typedef struct trie_node
{
    struct trie_node *children[ALPHABET_SIZE];
    bool is_word;
}
trie_node;

trie_node *create_trie_node(void);
void insert_trie(trie_node *root, const char *word);
bool search_trie(trie_node *root, const char *word);
bool starts_with(trie_node *root, const char *prefix);
void print_words(trie_node *node, char *prefix, int depth);
void free_trie(trie_node *root);

int main(void)
{
    printf("=== Trie Demo ===\n");
    trie_node *root = create_trie_node();
    
    if (root == NULL)
    {
        printf("Failed to create trie\n");
        return 1;
    }
    
    // Insert words
    const char *words[] = {"cat", "car", "card", "care", "careful", 
                          "cars", "carry", "dog", "dodge", "door"};
    int word_count = sizeof(words) / sizeof(words[0]);
    
    printf("Inserting words:\n");
    for (int i = 0; i < word_count; i++)
    {
        printf("Inserting '%s'\n", words[i]);
        insert_trie(root, words[i]);
    }
    
    // Search for words
    printf("\nSearching:\n");
    printf("Search for 'car': %s\n", search_trie(root, "car") ? "Found" : "Not found");
    printf("Search for 'cart': %s\n", search_trie(root, "cart") ? "Found" : "Not found");
    printf("Search for 'care': %s\n", search_trie(root, "care") ? "Found" : "Not found");
    
    // Check prefixes
    printf("\nPrefix checking:\n");
    printf("Words starting with 'car': %s\n", starts_with(root, "car") ? "Yes" : "No");
    printf("Words starting with 'xyz': %s\n", starts_with(root, "xyz") ? "Yes" : "No");
    
    // Print all words
    printf("\nAll words in trie:\n");
    char prefix[100] = "";
    print_words(root, prefix, 0);
    
    free_trie(root);
    return 0;
}

trie_node *create_trie_node(void)
{
    trie_node *node = malloc(sizeof(trie_node));
    if (node != NULL)
    {
        node->is_word = false;
        for (int i = 0; i < ALPHABET_SIZE; i++)
        {
            node->children[i] = NULL;
        }
    }
    return node;
}

void insert_trie(trie_node *root, const char *word)
{
    if (root == NULL || word == NULL)
        return;
    
    trie_node *current = root;
    
    for (int i = 0; word[i] != '\0'; i++)
    {
        int index = tolower(word[i]) - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE)
            continue; // Skip non-alphabetic characters
        
        if (current->children[index] == NULL)
        {
            current->children[index] = create_trie_node();
        }
        
        current = current->children[index];
    }
    
    current->is_word = true;
}

bool search_trie(trie_node *root, const char *word)
{
    if (root == NULL || word == NULL)
        return false;
    
    trie_node *current = root;
    
    for (int i = 0; word[i] != '\0'; i++)
    {
        int index = tolower(word[i]) - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE)
            continue;
        
        if (current->children[index] == NULL)
            return false;
        
        current = current->children[index];
    }
    
    return current->is_word;
}

bool starts_with(trie_node *root, const char *prefix)
{
    if (root == NULL || prefix == NULL)
        return false;
    
    trie_node *current = root;
    
    for (int i = 0; prefix[i] != '\0'; i++)
    {
        int index = tolower(prefix[i]) - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE)
            continue;
        
        if (current->children[index] == NULL)
            return false;
        
        current = current->children[index];
    }
    
    return true; // Prefix exists
}

void print_words(trie_node *node, char *prefix, int depth)
{
    if (node == NULL)
        return;
    
    if (node->is_word)
    {
        prefix[depth] = '\0';
        printf("%s\n", prefix);
    }
    
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (node->children[i] != NULL)
        {
            prefix[depth] = 'a' + i;
            print_words(node->children[i], prefix, depth + 1);
        }
    }
}

void free_trie(trie_node *root)
{
    if (root == NULL)
        return;
    
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (root->children[i] != NULL)
        {
            free_trie(root->children[i]);
        }
    }
    
    free(root);
}
