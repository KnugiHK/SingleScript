#include <stdio.h>
// This is an implementation of calculating the date of Easter.
// Based on: https://github.com/dateutil/dateutil/blob/master/dateutil/easter.py

int main(){
    int y;
    printf("Enter year: ");
    scanf("%d", &y);
    int g = y % 19;
    int e = 0;

    int c = y / 100;
    int h = (c - c / 4 - (8 * c + 13) / 25 + 19 * g + 15) % 30;
    int i = h - (h / 28) * (1 - (h /28)*(29 / (h + 1)) * ((21 - g) / 11));
    int j = (y + y / 4 + i + 2 - c + c / 4) % 7;

    int p = i - j + e;
    int d = 1 + (p + 27 + (p + 6) / 40) % 31;
    int m = 3 + (p + 26) / 30;
    if (m == 4){
        printf("April %d\n", d);
    }else if (m == 3){
        printf("March %d\n", d);
    }
    return 0;
}
