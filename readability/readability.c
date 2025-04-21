#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main (void)
{
    // prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    float L = (letters / (float)words) * 100;
    float S = (sentences / (float) words) * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
    // Print the grade level
    printf("Grade %d\n",(int)round(index));
    }
}

int count_letters(string text) {
    int letters = 0;
    for (int i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            letters++;
        }
    }
    return letters;
}

// Return the number of words in text
int count_words(string text)
{
    int words = 1;
    // Start with 1 to account for the last word

    for (int i= 0 ; i < strlen(text); i++)
    {
        if (text[i] == ' ' )
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text) {
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            sentences++;
        }
    }
    return sentences;
}
