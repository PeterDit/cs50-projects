#include <cs50.h>
#include <stdio.h>

void print_row(int bricks, int height);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    int j;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
        print_row(i + 1,n);
    }
}
void print_row(int bricks, int height)
{
    for (int i = 0; i < (height - bricks); i++)
    {
        printf(" ");
    }
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}
