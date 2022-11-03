CFLAGS=-Wall -Wextra -std=c11 -pedantic -ggdb
LIBS=-lm

main: main.o
	$(CC) $(CFLAGS) -o main main.o $(LIBS)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c -o main.o $(LIBS)