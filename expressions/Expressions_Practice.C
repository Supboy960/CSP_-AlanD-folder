// Alan De Lara, Expressions Practice - C

#include <stdio.h>  
#include <math.h>

int var_one = 7-24/8*4+6;
int var_two = 18/3-7+2*5;
int var_three = 6*4/12+72/8-9;
int var_four = (17 - 6 / 2) + 4 * 3;
int var_five = -2*(1*4-2/2)+(6+2-3);
int var_six = -1 * ((3 - 4 * 7) / 5) - 2 * 24 / 6;
int var_seven = (3*pow(5,2) / 15) - (5 - pow(2,2));
int main(void) {  
printf("%d,%d,%d,%d,%d,%d,%d", var_one, var_two, var_three, var_four, var_five, var_six, var_seven);  
return 0;  
}  