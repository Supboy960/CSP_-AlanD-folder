//Alan De Lara, Update Financial Calculator - C

#include <stdio.h>

float inputs(char* type, float* input){
    printf("What is your monthly %s cost:\n", type);
    scanf("%f", input);
    return *input;
}

void display(float cost, float income, const char* type) {  
    float percent = (cost / income) * 100;  
    printf("Your %s is $%.2f, which is %.2f%% of your income.\n", type, cost, percent);  
}



float spendings;
float savings;
float rent;
float income;
float utilities;
float groceries;
float transportation;


int main(void){
    
printf("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.\n");

income= inputs("income", &income);
rent = inputs("rent", &rent);
utilities = inputs("utilities", &utilities);
groceries = inputs("groceries", &groceries);
transportation = inputs("transportation", &transportation);

savings = income*0.1;
spendings = income-savings-rent-utilities-groceries-transportation;


display(rent, income, "rent");  
display(utilities, income, "utilities");  
display(groceries, income, "groceries");  
display(transportation, income, "transportation");  
display(savings, income, "savings");  
display(spendings, income, "spendings");  


    return 0;
}

