#Alan De Lara, Old Enough- Python

print("Welcome to my old enough program that tells you whether you are old enough to vote, drive, get a learners permit, and go to school. (Don't take the advice given seriously from this program, this only for entertainment purposes only.)")

age = input("What is your age(in years!):\n")

if age < 5:
    print("You aren't old enough to go to school, you can't get your get your learner's permit, drive, or vote.\nHow are you running this program?\nHow can you even read this?!?\n")
elif age >= 18:
    print("You are old enough to vote, drive, get your learner's permit, and (should be) go to school.\n")
elif age >= 16:
    print("You are old enough to drive. Hopefully you know what to do at a red light!...(SLAM THE GAS!!!!)\n")
elif age >= 15:
    print("You are old enough to get your learner's permit. Exciting, but be careful!\n")
else:
    print("You are old enough and should be going to school.\n")