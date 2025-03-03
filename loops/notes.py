#Alan De Lara, Loops notes python 
#
#1. What is a loop? 
    #A section of code the replests mulitplu times
#2 What are the two types of loops?
#For Loop
nums = [12,3,66,7,3,2]

for num in nums:
    print(num)

    #while loop
x = 0

while x < 10:
    print(x)
    x+= 1 
#3 What is iteration
    #That specific instance of the loop
    #iteration the amout of times you are looping through

#4 What are lists? 
#A list is a varibale the holds miltle numbers

nums = [1,2,3,4,5,6,7,6]
siblings = ["Alan", "Melaine", "Aaron", "Melissa", "(I forgot her name)"]
print(nums) #print whole list is ugly
print(siblings [3]) #prints 1 item from the list

siblings[4] = "Cute baby"
siblings.pop(3)
siblings.insert(1, "Jake")
siblings.insert(2,["Joe", "Noah", "Zee"])
print(siblings)
#5 How do you make lists in python? 
#Setp 1: use brackets
#setp 2; 
#Step 3:
#6 How do you make for loops in python? 
for sibling in siblings:
    print(sibling)

for x in range(0,101, 20):
    print(x)
#7 How do you make while loops in python?
import random
x = 1 #varible to keep counr of iteration
goose = random.randint(1,20)


while x <= 20:
    if x == goose:
    print("Goose!")
    break #tells th loop to stop
else:
    print("Duck")
    x+=1

    #Continue; moves on to the next interation without fishimng 
#8 How do you make lists in C?
#9 How do you make for loops in C?
#10 How do you make while loops in C?
