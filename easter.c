#include <stdio.h>
// This is an implementation on calculating the date of Easter.
// Based on: https://github.com/dateutil/dateutil/blob/master/dateutil/easter.py

int main(){
    int g, e, y, h, i, j, p, d, m, c;
    printf("Enter year: ");
    scanf("%d", &y);
    g = y % 19;
    e = 0;

    c = y / 100;
    h = (c - c / 4 - (8 * c + 13) / 25 + 19 * g + 15) % 30;
    i = h - (h / 28)*(1 - (h /28)*(29 / (h + 1))*((21 - g) / 11));
    j = (y + y / 4 + i + 2 - c + c / 4) % 7;

    p = i - j + e;
    d = 1 + (p + 27 + (p + 6) / 40) % 31;
    m = 3 + (p + 26) / 30;
    if (m == 4){
        printf("April %d\n", d);
    }else if (m == 3){
        printf("March %d\n", d);
    }
    return 0;
}
