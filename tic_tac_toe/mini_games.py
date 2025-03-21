# Tic-Tac-Toe Game with 3 Difficulty Levels

# Variable to store the game board
board = [" " for _ in range(9)]

# Function 1: Display the game board and key
def display_board():
    """Display the current game board and position key."""
    print("\nGame Board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    print("\nKey for Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print("\n")

# Function 2: Check for a winner
def check_winner():
    """Check if there is a winner or if the game ends in a tie."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Tie"
    return None

# Mini AI: Make a move based on difficulty
def ai_move(difficulty):
    """AI makes a move based on the selected difficulty level."""
    if difficulty == "easy":
        # Easy AI chooses the first available position
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                return

    elif difficulty == "medium":
        # Medium AI blocks the player from winning when possible
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_winner() == "X":
                    board[i] = "O"
                    return
                board[i] = " "
        # If no blocking move, choose the first available position
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                return

    elif difficulty == "hard":
        # Hard AI tries to win or block the player strategically
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_winner() == "O":
                    return
                board[i] = "X"
                if check_winner() == "X":
                    board[i] = "O"
                    return
                board[i] = " "
        # If no strategic move is found, pick the center if available
        if board[4] == " ":
            board[4] = "O"
            return
        # Else choose the first available position
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                return

# Play against the AI
def play_against_ai(difficulty):
    """Player plays against the AI at the selected difficulty level."""
    global board
    board = [" " for _ in range(9)]
    display_board()
    current_player = "X"

    while " " in board:
        if current_player == "X":
            # Player's turn
            try:
                move = int(input("Your turn! Choose a position (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = "X"
                    display_board()

                    # Check for a winner
                    winner = check_winner()
                    if winner:
                        if winner == "X":
                            print("Congratulations! You win!")
                        elif winner == "O":
                            print("AI wins! Better luck next time.")
                        else:
                            print("It's a tie!")
                        break

                    # Switch to AI
                    current_player = "O"
                else:
                    print("Position already taken. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a position between 1 and 9.")
        else:
            # AI's turn
            print("AI's turn...")
            ai_move(difficulty)
            display_board()

            # Check for a winner
            winner = check_winner()
            if winner:
                if winner == "X":
                    print("Congratulations! You win!")
                elif winner == "O":
                    print("AI wins! Better luck next time.")
                else:
                    print("It's a tie!")
                break

            # Switch back to Player
            current_player = "X"

# Main menu to choose difficulty
def main_menu():
    """Main menu to choose game options."""
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print("\nChoose a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            play_against_ai("easy")
        elif choice == "2":
            play_against_ai("medium")
        elif choice == "3":
            play_against_ai("hard")
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Start the game
main_menu()

