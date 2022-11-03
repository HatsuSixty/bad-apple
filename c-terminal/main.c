#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define INPUT_TXT_PATH "input.txt"

#define WIDTH 36
#define HEIGHT 28
#define FRAMES 4381

void read_file_into_bytearray(char** bytearray, FILE* file)
{
    fseek(file, 0, SEEK_END);
    size_t filelen = ftell(file);
    rewind(file);

    *bytearray = (char*)malloc(sizeof(char) * filelen);
    fread(*bytearray, filelen, 1, file);
}

int msleep(long msec)
{
    struct timespec ts;
    int res;

    if (msec < 0)
    {
        errno = EINVAL;
        return -1;
    }

    ts.tv_sec = msec / 1000;
    ts.tv_nsec = (msec % 1000) * 1000000;

    do {
        res = nanosleep(&ts, &ts);
    } while (res && errno == EINTR);

    return res;
}

int main(void)
{
    printf("Starting in 3...\n");
    sleep(1);
    printf("Starting in 2...\n");
    sleep(1);
    printf("Starting in 1...\n");
    sleep(1);
    printf("Starting...\n");
    printf("\033[4A");
    fflush(stdout);

    FILE* file = fopen(INPUT_TXT_PATH, "rb");
    if (file == NULL) {
        fprintf(stderr, "ERROR: Could not open file `%s`: %s\n", INPUT_TXT_PATH, strerror(errno));
        exit(1);
    }

    char* buffer = NULL;
    read_file_into_bytearray(&buffer, file);
    fclose(file);

    size_t offset = 0;
    for (size_t f = 0; f < FRAMES; ++f) {
        for (size_t c = 0; c < WIDTH*HEIGHT+HEIGHT; ++c) {
            if (buffer[offset+c] == '1') { printf("\033[30;40m"); }
            else                         { printf("\033[37;47m"); }
            printf("%c ", buffer[offset+c]);
        }
        printf("\033[%dA", HEIGHT);
        fflush(stdout);
        printf("\033[%dD", WIDTH);
        fflush(stdout);
        offset += WIDTH*HEIGHT+HEIGHT;
        msleep(51);
    }
    printf("\033[m");

    return 0;
}