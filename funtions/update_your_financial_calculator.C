//Alan De Lara, Update Financial Calculator - C

#include <stdio.h>  
  
void inputs(char type[20], float *input){   
    printf("What is your monthly %s cost:\n", type);  
    scanf("%f", input);   
}  
  
float income;  
float utilities;  
float groceries;  
float transportation;  
float rent; 
int main(void){  
    printf("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.\n");  
  
    inputs("income", &income);  
    inputs("rent", &rent);  
    inputs("utilities", &utilities);  
    inputs("groceries", &groceries);  
    inputs("transportation", &transportation);  
  
    float savings = income * 0.1;  
    float spending = income - (rent + utilities + groceries + transportation + savings);  
  
    
     
  
    void display(float cost, float income, const char* type) {  
        float percent = (cost / income) * 100;  
        printf("Your %s is $%.2f, which is %.2f%% of your income.\n", type, cost, percent);  
    }
    

float percent_of_rent = display(rent, income, "rent");  
float percent_of_utilities = display(utilities, income, "utilities");
float percent_of_groceries = display(groceries, income, "groceries");
float percent_of_transportation = display(transportation, income, "transportation");
float percent_of_savings = display(savings, income, "savings");
float  percent_of_spending = display(spending, income, "spending");
 
printf("Your rent is $%.2f which is %.2f%% of your income.\n", rent, percent_of_rent);  
printf("Your utilities are $%.2f which is %.2f%% of your income.\n", utilities, percent_of_utilities);  
printf("Your groceries are $%.2f which is %.2f%% of your income.\n", groceries, percent_of_groceries);  
printf("Your transportation is $%.2f which is %.2f%% of your income.\n", transportation, percent_of_transportation);  
printf("Your savings is $%.2f which is %.2f%% of your income.\n", savings, percent_of_savings);
printf("Your spending is $%.2f which is %.2f%% of your income.\n", spending, percent_of_spending);

    
    
    
    return 0;  

}  
