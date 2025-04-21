#include <stdio.h>
#include <cs50.h>
int main (void)
{
    char greetings[30];
    printf("What is your name?\n");
    scanf("%s", greetings);
    printf("hello, %s\n", greetings);
}

