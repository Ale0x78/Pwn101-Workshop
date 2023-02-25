#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

#include <stdint.h>

void vulnrable_function(void)
{
    char buffer[100];

    printf("Enter shellcode:\n");
    memset(buffer, 0x00, 100);
    read(0, buffer, 90);

    for (int i = 0; i < 100; i++)
    {
        if (buffer[i] != '\x90' && buffer[i] != '\x00' && buffer[i] != '\n')
        {
            printf("Your shellcode includes things other then 0x90 (NOP) and NULL bytes (0x00)[%x]\n", buffer[i]);
            exit(23);
        }
    }

    printf("Your shellcode is at %p, you may now change 8 byte chunks in there\n", buffer);

    printf("What idx do you want to write to?\n");
    int idx = 0;
    while (scanf("%d", &idx) == 1)
    {
        printf("What value do you want to write to idx=%d?\n", idx);
        uint64_t val = 0;
        scanf("%lu", &val);
        *((uint64_t *)(buffer + idx)) = val;
        printf("What idx do you want to write to?\n");
    }
    printf("Done! I am not running the shellcode though :)\n");

    // ((void (*)())buffer)();
}

void main(void)
{
    vulnrable_function();
}