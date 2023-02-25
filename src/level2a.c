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
    read(0, buffer, 100);
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
