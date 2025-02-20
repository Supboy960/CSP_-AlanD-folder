#Alan De Lara, Update Financial Calculator - Python

def info(cost, income, type ):
    percent= cost/income*100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")


print("Welcome to the Financial Calculator! This program will help you analyze your income and expenses.")

def collecting_data(type):
    return input(f"What is your monthly {type}")
    
def collect_inputs():  
    income = float(collecting_data("income"))  
    rent = float(collecting_data("rent"))  
    utilities = float(collecting_data("utilities"))  
    groceries = float(collecting_data("groceries"))  
    transportation = float(collecting_data("transportation"))  
    return income, rent, utilities, groceries, transportation  


income = float(collecting_data("income:\n"))
rent = float(collecting_data("rent:\n"))
utilities = float(collecting_data("utilities:\n"))
groceries = float(collecting_data("groceries:\n"))
transportation = float(collecting_data("transportation:\n"))

savings = income*0.1

spending = income-rent-utilities-groceries-transportation

percent = rent/income*0.1




info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
