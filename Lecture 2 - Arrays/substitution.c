#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool is_valid_key(string key);

int main(int argc, string argv[])
{
    // Check for correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    
    string key = argv[1];
    
    // Validate key
    if (!is_valid_key(key))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }
    
    // Get plaintext
    string plaintext = get_string("plaintext: ");
    
    printf("ciphertext: ");
    
    // Encrypt each character
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];
        
        if (isalpha(c))
        {
            if (isupper(c))
            {
                printf("%c", toupper(key[c - 'A']));
            }
            else
            {
                printf("%c", tolower(key[c - 'a']));
            }
        }
        else
        {
            printf("%c", c);
        }
    }
    
    printf("\n");
    return 0;
}

bool is_valid_key(string key)
{
    // Check length
    if (strlen(key) != 26)
    {
        return false;
    }
    
    // Check for alphabetic characters and duplicates
    bool used[26] = {false};
    
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }
        
        int index = toupper(key[i]) - 'A';
        if (used[index])
        {
            return false;
        }
        used[index] = true;
    }
    
    return true;
}
