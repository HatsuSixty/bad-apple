CFLAGS=-Wall -Wextra -std=c11 -pedantic -ggdb `pkg-config --cflags SDL2_mixer`
LIBS=`pkg-config --libs SDL2_mixer` -lm

main: main.o
	$(CC) $(CFLAGS) -o main main.o $(LIBS)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c -o main.o $(LIBS)