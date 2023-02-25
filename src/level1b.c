#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct user_struct
{
    char name[8];
    unsigned int canary;
    int admin;

} __attribute__((packed)) typedef user;

int main()
{
    user user1;
    user1.canary = 0xdeadbeef;
    user1.admin = 0x0;
    printf("Enter a string:\n");
    gets(user1.name); // This is the vulnerable function that allows for buffer overflow
    if (user1.canary != 0xdeadbeef)
    {
        printf("Hacking attemped!");
        printf("It will be my turn to get angry soon,' he said. 'If you say that again, I shall. Then you will see Gandalf the Grey uncloaked.\n");
        return 0;
    }
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
