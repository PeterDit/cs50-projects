#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc == 2)
    {
        // Make sure every character in argv[1] is a digit
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        // Convert argv[1] from a string to an int
        int key = atoi(argv[1]);

        // Prompt user for plaintext
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        // Rotate each character in the plaintext
        for (int i = 0, len = strlen(plaintext); i < len; i++)
        {
            if (isalpha(plaintext[i]))
            {
                char rotated = plaintext[i]; // Initialize with the current character
                if (isupper(plaintext[i]))
                {
                    rotated = ((plaintext[i] - 'A' + key) % 26) + 'A';
                }
                else if (islower(plaintext[i]))
                {
                    rotated = ((plaintext[i] - 'a' + key) % 26) + 'a';
                }
                printf("%c", rotated);
            }
            else
            {
                printf("%c", plaintext[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
