// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

void to_lowercase(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = tolower(str[i]);
    }
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Declare and initialize hash_value
    int hash_value = hash(word);

    // Initialize current_node
    node *current_node = table[hash_value];

    char lower_word[LENGTH + 1];
    strcpy(lower_word, word);
    to_lowercase(lower_word);

    while (current_node != NULL)
    {
        char lower_current_word[LENGTH + 1];
        strcpy(lower_current_word, current_node->word);
        to_lowercase(lower_current_word);

        if (strcmp(lower_current_word, lower_word) == 0)
        {
            return true;
        }
        current_node = current_node->next;
    }
    return false;
}
// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int P = 1031;
    int hash_value = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        char c = toupper(word[i]);
        hash_value = (hash_value * 31 + c) % P;
    }
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        strcpy(n->word, buffer);
        int index = hash(buffer);
        n->next = table[index];
        table[index] = n;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int counter = 0;

    for (int i = 0; i < N; i++)
    {
        node *current_node = table[i];

        while (current_node != NULL)
        {
            counter++;
            current_node = current_node->next;
        }
    }
    return counter;
}
// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int bucket = 0; bucket < N; bucket++)
    {
        node *current_node = table[bucket];
        while (current_node != NULL)
        {
            node *temp_node = current_node;
            current_node = current_node->next;
            free(temp_node);
        }
    }
    return true;
}
