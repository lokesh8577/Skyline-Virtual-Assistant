import random
print("welcome in snake water game")
computer = ['S','W','G']

i=1
while(i<=3):
    user = input("enter your choice: gun,snake,water ")
    user_choice=user.upper()
    print(user_choice[0])
    random_int = random.randint(0, 2)
    computer_choice=computer[random_int]
    print(f"Computer choice = {computer_choice}")
    if (computer_choice == 'G' and user_choice[0] == 'W') or \
       (computer_choice == 'W' and user_choice[0] == 'S') or \
       (computer_choice == 'S' and user_choice[0] == 'G'):
         print("user Win!")
       
    elif(computer_choice==user_choice[0]):
         print("Draw!")
    else:
         print("Computer Win!") 

    i+=1

print('Thank you for playing snake water game')
