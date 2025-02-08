//Alan De Lara, Financial Calculator - C

#include <stdio.h>

int main(void) {
    // Print statement that welcomes the user and tells what the program does
    printf("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.\n");

    // Declare variables for income and expenses
    float income, rent, utilities, groceries, transportation, savings, spending;
    float percent_of_rent, percent_of_utilities, percent_of_groceries, percent_of_transportation, percent_of_spending, savings_percentage;

    // Ask for the user's income and expenses
    printf("What is your income?\n");
    scanf("%f", &income);

    printf("What is your rent?\n");
    scanf("%f", &rent);

    printf("What are your utilities?\n");
    scanf("%f", &utilities);

    printf("What are your groceries?\n");
    scanf("%f", &groceries);

    printf("What is your transportation?\n");
    scanf("%f", &transportation);

    // Calculate savings as 10% of income (income * 0.1)
    savings = income * 0.1;

    // Calculate spending as income minus all expenses, including savings
    spending = income - (rent + utilities + groceries + transportation + savings);

    // Calculate percentages of income
    percent_of_rent = (rent / income) * 100;
    percent_of_utilities = (utilities / income) * 100;
    percent_of_groceries = (groceries / income) * 100;
    percent_of_transportation = (transportation / income) * 100;
    savings_percentage = (savings / income) * 100;
    percent_of_spending = (spending / income) * 100;

    // Print the results
    printf("Your rent is $%.2f which is %.2f%% of your income.\n", rent, percent_of_rent);
    printf("Your utilities are $%.2f which is %.2f%% of your income.\n", utilities, percent_of_utilities);
    printf("Your groceries are $%.2f which is %.2f%% of your income.\n", groceries, percent_of_groceries);
    printf("Your transportation is $%.2f which is %.2f%% of your income.\n", transportation, percent_of_transportation);
    printf("Your savings is $%.2f which is %.2f%% of your income.\n", savings, savings_percentage);
    printf("Your spending is $%.2f which is %.2f%% of your income.\n", spending, percent_of_spending);

    return 0;
}