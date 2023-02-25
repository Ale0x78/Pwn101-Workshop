CC=gcc
CFLAGS=-Wall -Wextra -O0 -pedantic -std=c11 -z execstack

all: level1a level1b level2a level2b
level1a: src/level1a.c
	$(CC) $(CFLAGS) src/level1a.c -o release/level1a

level1b: src/level1b.c
	$(CC) $(CFLAGS) src/level1b.c -o release/level1b

level2a: src/level2a.c
	$(CC) $(CFLAGS) src/level2a.c -o release/level2a

level2b: src/level2b.c
	$(CC) $(CFLAGS) src/level2b.c -o release/level2b

clean:
	cd release; rm -f level1a level1b level2a level2b; cd -
