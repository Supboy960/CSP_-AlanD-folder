//Alan De Lara, Update Financial Calculator - C

#include <stdio.h>  
  
// Function to collect user input  
void collect_inputs(double *income, double *rent, double *utilities, double *groceries, double *transportation) {  
    printf("Enter your monthly income: ");  
    scanf("%lf", income);  
    printf("Enter your monthly rent: ");  
    scanf("%lf", rent);  
    printf("Enter your monthly utilities: ");  
    scanf("%lf", utilities);  
    printf("Enter your monthly groceries: ");  
    scanf("%lf", groceries);  
    printf("Enter your monthly transportation: ");  
    scanf("%lf", transportation);  
}  
  
// Function to calculate and print the percentage of income for each expense  
void calculate_percentages(double income, double rent, double utilities, double groceries, double transportation) {  
    double savings = income * 0.1;  
    double spending = income - rent - utilities - groceries - transportation;  
  
    printf("Rent is %.2f%% of your income.\n", (rent / income) * 100);  
    printf("Utilities are %.2f%% of your income.\n", (utilities / income) * 100);  
    printf("Groceries are %.2f%% of your income.\n", (groceries / income) * 100);  
    printf("Transportation is %.2f%% of your income.\n", (transportation / income) * 100);  
    printf("Savings is %.2f%% of your income.\n", (savings / income) * 100);  
    printf("Spending is %.2f%% of your income.\n", (spending / income) * 100);  
}  
  
int main() {  
    double income, rent, utilities, groceries, transportation;  
  
    printf("Welcome to the Financial Calculator!\n");  
    collect_inputs(&income, &rent, &utilities, &groceries, &transportation);  
    calculate_percentages(income, rent, utilities, groceries, transportation);  
  
    return 0;  
}  
