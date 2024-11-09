import random

print("Welcome to guess the number game")
number = random.randint(1, 100)
choice = 0

while True:
    user_input = int(input("Enter a number between 1 and 100: "))
    choice += 1
    
    if user_input > number:
        print("Your number is greater than the random number.")
    elif user_input < number:
        print("Your number is less than the random number.")
    else:
        print("Congratulations! You win!")
        print(f"You tried {choice} times.")
        break
