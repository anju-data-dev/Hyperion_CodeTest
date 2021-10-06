# NUMBER GUESSING GAME

import random

number = random.randint(1,20)
print("\n Welcome to Number Guessing Game!!!\n There are 5 rounds in a game. \n Here you go... \n All the best!\n")
player_name = input("Enter your Name: ")
game_round = 1

while game_round <= 5:
    user_choice = input("Enter a number between 1 to 20: ")
    user_choice = int(user_choice)
    
    if user_choice == number:
        print(f"Congratulations {player_name}!!! You Won!!!")
        break

    elif user_choice < number:
        print("Your guess is low")
            
    else:        
        print("Your guess is high")
                
    game_round+=1 
        
print(f"Hey {player_name}, Thank You for playing!!! Bye !!!")      



