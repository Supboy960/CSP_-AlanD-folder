#Alan De Lara, Old Enough- Python

# Douglas London, Old enough python

print("Welcome to my old enough program that tells you whether you are old enough to vote, drive, get a learners permit, and go to school.")

age = input("What is your age:\n")

if age >= 18:
    print("You can vote, drive, get a learners pemit, and go to school.\n")
elif age >= 16:
        print("you can drive, get a learners permit, and go to school.\n")
elif age >= 15:
        print("You can get a learners permit and go to school.\n")
elif age < 5 :
        print("How are you on this program if you don't know numbers or how to read? You can't go to school, get your learner's permit, drive, or vote....(yet)\n")
else:
    print("You get to learn at school!...YAY!\n")