words = ["pattern", "hay", "overview", "anniversary", "flourish", "remember", "experiment"]  
import random  
  
chosen_word = random.choice(words)  
  
def display_hangman(chosen_word, guessed_letters):  
    display = ""  
    for letter in chosen_word:  
        if letter in guessed_letters:  
            display += letter  
        else:  
            display += "_"  
    print(display)  
  
def check_guess(letter, chosen_word, guessed_letters):  
    if letter in chosen_word:  
        guessed_letters.append(letter)  
        return True  
    else:  
        return False  
  
guessed_letters = []  
wrong_attempts = 0  
max_attempts = 6        
  
while wrong_attempts < max_attempts:  
    display_hangman(chosen_word, guessed_letters)  
    letter = input("Guess a letter: ")  
      
    # Input validation: check if it's a single letter and not guessed before  
    if len(letter) == 1 and letter.isalpha():  
        if letter in guessed_letters:  
            print("You've already guessed that letter.")  
        else:  
            if check_guess(letter, chosen_word, guessed_letters):  
                print("Good guess!")  
            else:  
                wrong_attempts += 1  
                print("Wrong guess!")  
      
    # Check for win condition    
    if set(chosen_word).issubset(set(guessed_letters)):  
        print("Congratulations! You've guessed the word:", chosen_word)  
        break  # Exit the loop  
  
# Check for loss condition    
if wrong_attempts == max_attempts:  
    print("Game over! The word was:", chosen_word)  
   
