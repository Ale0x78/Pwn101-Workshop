#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct user_struct
{
    char name[8];
    int admin;
} __attribute__((packed)) typedef user;

int main()
{
    user user1;
    printf("Enter a string:\n");

    gets(user1.name); // This is the vulnerable function that allows for buffer overflow

    if (user1.admin != 0)
    {
        printf("CTF{BufferOverflowIsEasy}\n");
    }
    else
    {
        printf("Try again.\n");
    }

    return 0;
}
