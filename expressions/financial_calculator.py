# Alan De Lara, Financial Calculator python 

# print statment the welcomes user and tells what progame does

#ask what their income is (varible an inputs)
income = float (input ("what is your income?\n"))
#ask what their rent is (varible an inputs)
rent = float (input ("what is your rent?\n"))
#ask what their utlitities is (varible an inputs)
utilities = float (input ("what is your utlitities?\n"))
#ask what their groceries is (varible an inputs)
groceries = float (input ("what is your groceries?\n"))
#ask what their transportation is (varible an inputs)
transportation = float (input ("what is your transportation?\n"))
#calulate savings as 10% of income(income*.1) (variable)
savings = income/10
#Calualte spening as income-saving-rent-utilites-grocries-transpotation (variable)
spending = income-rent-utilities-groceries-transportation
#calulate percent income of rent (rent/income *100) (varible)\
percent_of_rent = rent/income *100
#calulate percent income of untilaiyes (utilalies/income *100) (varible)
percent_of_utilities = utilities/income *100
#calulate percent income of gorceries (gorceries/income *100) (varible)
percent_of_groceries = groceries/income *100
##calulate percent income of transportation (tansportation/income *100) (varible)
percent_of_transportation = transportation/income *100
#calulate percent income of spending (spending/income *100) (varible)
percent_of_spending = spending/income *100
#Your rent is $XX.XX which is XX% of income. (print)
print("You spend", rent "on rent and that is",percent_of_rent )
#Your untilyes is $XX.XX which is XX% of income. (print)

#Your grociers is $XX.XX which is XX% of income. (print)

#Your transportation is $XX.XX which is XX% of income. (print)

#Your savings is $XX.XX which is XX% of income. (print)

#Your spending is $XX.XX which is XX% of income. (print)