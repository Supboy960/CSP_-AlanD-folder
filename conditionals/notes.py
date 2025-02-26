#Alan De Lara, Conditionals Notes Python 
name = input("What is you name?;\n")
#1.What puts something inside of the “if” statement?  # it the Tab at the front 
if name == "LaRose":
    print("Hi Ms. LaRose")
else: # This happens if the condion is false
    print (f"Hello {name}!")

#2.What do if statements do? 
#Checks a conditons and if it is true it will do a thing
if name == "LaRose": #<= this is the condotion
    print("Hi Ms. LaRose")# <+ This is what it does if ture

#3.What are boolean statements? 
 
if name == "LaRose": # <= This is the boolean stament> it is either truse or false
    print("Hi Ms. LaRose")
else: # This happens if the condion is false
    print (f"Hello {name}!")#Just a true or false statement

#4.What do else statements do?
if name == "LaRose":
    print("Hi Ms. LaRose")
else: #if the booean is false, the else statement happens
    print (f"Hello {name}!")

#5.What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cokkies are ther?:\n"))
#computers read top to bottom, chack the least likly first
if num ==0: #<= if always starts the conditional
    print("There are none.")
elif num == 1: #Efverything in betwaeen schould be elif
    print("There is one.")
elif num <4: 
    print("There is are a couple")
elif num < 10:
    print("There are a few")
else: #,+ else always ends the onditional
    print("There are many.")
#6.What do each of the different symbols mean in conditionals? 
# < lees than
# > Greater than
# <= Less than or equal to
# >= Greather than or equal to
# == Equal to 
# === *Dosen't esist in Python, 
# ! Not 

#7.What are the 3 logical operators?
if num <10 and num >5: #And means both booleans must be true
    print("This is a big single digit number")
    
elif num <10 or num >5: #or means one booleans must be true
    print("This is a single digit number")

elif  not num <10 or num >5: #Not chages to check if flase
    print("This is a not single digit number")

#8.What are logical operators for?
    #Allows the code to handle more difficlut qestions ... increase compleity

#9.What does a nested conditional statement do?
if num <10: 
    if num ==8:
        print("this prints at 8")
    else:
        if num ==4:
            print("There are only engoh cookies left for me ... sorry")
        else:
            print("The number is less then 10")
else:
    print("The munber is bigger than 10") # You can east as meny contditionals you want but proble no more then 3
#10.How do you write an if statement in C?
#11.How do you write else statements in C?
#12.How do you write elif/ else if statements in C?
#13.How do you write the 3 logical operators in C?