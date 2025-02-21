//Alan De Lara, Update Financial Calculator - C

#include <stdio.h>

float inputs(char type[20], int input[50]){
    printf("What is your monthly %s cost:\n", type);
    scanf("%f", &input);
    return;
}

float income;
float utilities;
float groceries;
float transportation;


int main(void){
    
printf("Welcome to the Financial Calculator! This program will help you analyze your income and expenses."\n);
printf("What is your monthly income:\n");
scanf("%f", income);
printf("What is your monthly utilities:\n");
scanf("%f", utilities);
printf("What is your monthly groceries:\n");
scanf("%f", groceries);
printf("What is your monthly transportation:\n");
scanf("%f", transportation);


float rent = inputs("rent", 0);
float rent = inputs("rent", 0);







    return 0;
}