#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int ans = 0;
    FILE *fptr = fopen("input_edit.txt", "r");
    char *line = NULL;
    size_t len;
    ssize_t read;
    while ((read = getline(&line, &len, fptr)) != -1) {
        size_t line_len = strlen(line);
        int flag_i = 1, flag_j = 1;
        for (int i = 0, j = line_len - 2; flag_i || flag_j; ++i, --j) {
            if (flag_i && line[i] >= '0' && line[i] <= '9') {
                flag_i = 0;
                ans += (line[i] - '0') * 10;
            }
            if (flag_j && line[j] >= '0' && line[j] <= '9') {
                flag_j = 0;
                ans += line[j] - '0';
            }
        }
    }
    fclose(fptr);
    free(line);
    printf("\nans: %d", ans);
    return 0;
}