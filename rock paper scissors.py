import tkinter as tk
import random

def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def button(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)

    result = winner(choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")
 
# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("600x400")
window.configure(bg = "#EE1289")

# Create labels and buttons with larger fonts and buttons
instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Times New Roman", 20))
instruction_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: button("Rock"), font=("Times New Roman", 16), padx=20, pady=10)
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", command=lambda: button("Paper"), font=("Times New Roman", 16), padx=20, pady=10)
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: button("Scissors"), font=("Times New Roman", 16), padx=20, pady=10)
scissors_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Times New Roman", 16))
result_label.pack()

# Start the main loop
window.mainloop()
