#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>

#define SZ 4

void extractNumbers(const char *inputString, int *numbers) {
    int count = 0;
    while (*inputString) {
        while (*inputString && !isdigit(*inputString)) {
            inputString++;
        }
        if (*inputString) {
            numbers[count++] = atoi(inputString);
            while (*inputString && isdigit(*inputString)) {
                inputString++;
            }
        }
    }
}

int main(int argc, char *argv[]) {
    char *line = NULL;
    size_t len;
    ssize_t read;
    FILE *fptr = fopen("input.txt", "r");
    int time[SZ];
    int distance[SZ];
    int curr = 0;
    while ((read = getline(&line, &len, fptr)) != -1) {
        if (!curr)
            extractNumbers(line, time);
        else
            extractNumbers(line, distance);
        curr++;
    }
    fclose(fptr);
    free(line);

    for (int i = 0; i < SZ; ++i) {
        printf("\ntime: %d, distance: %d", time[i], distance[i]);
    }

    int ans = 1;
    for (int i = 0; i < SZ; ++i) {
        int curr = 0;
        for (int j = 1; j < time[i]; ++j) {
            if ((time[i] - j) * j > distance[i]) {
                curr++;
            }
        }
        ans *= curr; 
    }
    printf("\nans: %d", ans);
    return 0;
}