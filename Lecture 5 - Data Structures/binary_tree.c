#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct treenode
{
    int data;
    struct treenode *left;
    struct treenode *right;
}
treenode;

treenode *create_tree_node(int value);
void insert_node(treenode **root, int value);
void inorder_traversal(treenode *root);
void preorder_traversal(treenode *root);
void postorder_traversal(treenode *root);
bool search_tree(treenode *root, int value);
int tree_height(treenode *root);
void free_tree(treenode *root);

int main(void)
{
    printf("=== Binary Tree Demo ===\n");
    treenode *root = NULL;
    
    // Insert nodes
    insert_node(&root, 50);
    insert_node(&root, 30);
    insert_node(&root, 70);
    insert_node(&root, 20);
    insert_node(&root, 40);
    insert_node(&root, 60);
    insert_node(&root, 80);
    
    printf("Tree structure:\n");
    printf("       50\n");
    printf("      /  \\\n");
    printf("    30    70\n");
    printf("   / \\   / \\\n");
    printf("  20 40 60 80\n\n");
    
    printf("In-order traversal: ");
    inorder_traversal(root);
    printf("\n");
    
    printf("Pre-order traversal: ");
    preorder_traversal(root);
    printf("\n");
    
    printf("Post-order traversal: ");
    postorder_traversal(root);
    printf("\n");
    
    printf("Tree height: %d\n", tree_height(root));
    
    printf("Search for 40: %s\n", search_tree(root, 40) ? "Found" : "Not found");
    printf("Search for 90: %s\n", search_tree(root, 90) ? "Found" : "Not found");
    
    free_tree(root);
    return 0;
}

treenode *create_tree_node(int value)
{
    treenode *new_node = malloc(sizeof(treenode));
    if (new_node != NULL)
    {
        new_node->data = value;
        new_node->left = NULL;
        new_node->right = NULL;
    }
    return new_node;
}

void insert_node(treenode **root, int value)
{
    if (*root == NULL)
    {
        *root = create_tree_node(value);
        return;
    }
    
    if (value < (*root)->data)
    {
        insert_node(&((*root)->left), value);
    }
    else if (value > (*root)->data)
    {
        insert_node(&((*root)->right), value);
    }
    // Ignore duplicates
}

void inorder_traversal(treenode *root)
{
    if (root != NULL)
    {
        inorder_traversal(root->left);
        printf("%d ", root->data);
        inorder_traversal(root->right);
    }
}

void preorder_traversal(treenode *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preorder_traversal(root->left);
        preorder_traversal(root->right);
    }
}

void postorder_traversal(treenode *root)
{
    if (root != NULL)
    {
        postorder_traversal(root->left);
        postorder_traversal(root->right);
        printf("%d ", root->data);
    }
}

bool search_tree(treenode *root, int value)
{
    if (root == NULL)
        return false;
    
    if (root->data == value)
        return true;
    else if (value < root->data)
        return search_tree(root->left, value);
    else
        return search_tree(root->right, value);
}

int tree_height(treenode *root)
{
    if (root == NULL)
        return -1;
    
    int left_height = tree_height(root->left);
    int right_height = tree_height(root->right);
    
    return 1 + (left_height > right_height ? left_height : right_height);
}

void free_tree(treenode *root)
{
    if (root != NULL)
    {
        free_tree(root->left);
        free_tree(root->right);
        free(root);
    }
}
