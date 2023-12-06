#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>

void get_input(const char *source, char *dest) {
    while (*source != '\0') {
        if (isdigit(*source)) {
            *dest = *source;
            dest++;
        }
        source++;
    }
    *dest = '\0';
}

int main(int argc, char *argv[]) {
    char *line = NULL;
    size_t len;
    ssize_t read;
    FILE *fptr = fopen("input.txt", "r");
    char time_str[100];
    char distance_str[100];
    int curr = 0;
    while ((read = getline(&line, &len, fptr)) != -1) {
        if (!curr)
            get_input(line, time_str);
        else
            get_input(line, distance_str);
        curr++;
    }
    fclose(fptr);
    free(line);

    long long time = strtoll(time_str, NULL, 10);
    long long distance = strtoll(distance_str, NULL, 10);

    int ans = 0;
    for (int i = 1; i < time; ++i) {
        if ((time - i) * i > distance) {
            ans++;
        }
    }
    printf("\nans: %d", ans);
    return 0;
}