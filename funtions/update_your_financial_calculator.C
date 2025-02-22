//Alan De Lara, Update Financial Calculator - C

#include <stdio.h>  
  
float inputs(char type[20]){   
    printf("What is your monthly %s cost:\n", type);   
}  
float display(float cost, float income, const char* type) {  
    float percent = (cost / income) * 100;  
    printf("Your %s is $%.2f, which is %.2f%% of your income.\n", type, cost, percent);  
}
  
 
 

int main(void){  
    printf("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.\n");  
  
    float income = inputs("income"); // do this with the others
    scanf("%f", &income); 
    float rent = inputs("rent");  
    scanf("%f", &rent);
    float utilities = inputs("utilities");  
    scanf("%f", &utilities);
    float groceries = inputs("groceries");  
    scanf("%f", &groceries);
    float transportation = inputs("transportation");  
    scanf("%f", &transportation);
  
    float savings = income * 0.1;  
    float spending = income - (rent + utilities + groceries + transportation + savings);  
  
    
     
  

    

float percent_of_rent = display(rent, income, "rent");  
float percent_of_utilities = display(utilities, income, "utilities");
float percent_of_groceries = display(groceries, income, "groceries");
float percent_of_transportation = display(transportation, income, "transportation");
float percent_of_savings = display(savings, income, "savings");
float percent_of_spending = display(spending, income, "spending");
 

    
    
    
    return 0;  

}  
