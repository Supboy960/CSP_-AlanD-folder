#Alan De Lara, Update Financial Calculator - Python

def info(cost, income, type ):
    percent= cost/income*100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")


print("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.")

def collecting_data(type):
    return input(f"What is your monthly {type} cost:\n")
    
    
income = float(input("What is your monthly income:\n"))
rent = float(input("What is your monthly rent:\n"))
utilities = float(input("What is your monthly utilities:\n"))
groceries = float(input("What is your monthly groceries:\n"))
transportation = float(input("What is your monthly transportation:\n"))

savings = income*0.1

spending = income-rent-utilities-groceries-transportation

percent = rent/income*0.1




info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")






