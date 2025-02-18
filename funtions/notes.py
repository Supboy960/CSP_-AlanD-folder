# Alan De Lara, Funtions Notes Python

#Funtinos hold actions to be reused
#number = int(input("Please tell me a number:\n"))
#def add(numOne, numTwo): # paramneters set the name of the varible (just for the funtion)
    
   # return numOne + numTwo 
#print(add(number,21))#arguemnets set the value of the varible just for that instacen of the futnion.
#print(add(8,12))
#addition = add(6,4)
#print(add(addition,10000))
#add(87,3)

def values(type):
    return input(f"Please give me a {type}:\n")

name = values ("name")
place =values ("place")
verb =values ("verb (past tense)")

print(f"{name} was rlly fast getting to {place} becase the {verb} the whole way there.")