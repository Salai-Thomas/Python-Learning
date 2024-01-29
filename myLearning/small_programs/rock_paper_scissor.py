import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

items = [Rock,Scissor,Paper]

user_input = input('Choose Rock, Scissor <or/> Paper : ')

system_choice = random.randint(0,2)

print(user_input)

def play_ground(user_input,system_choice):
    if user_input == system_choice:
        print('Draw!')
    elif user_input == 1 and system_choice == 2:
        print('You Win!')
    else:
        print('You Lose!')

match user_input:
    case 'rock':
        user_input = 0
        print(f'You choose Rock!{items[user_input]}')
        print(f'system choose = {items[system_choice]}')
        play_ground(user_input,system_choice)
    case 'scissor':
        user_input = 1
        print(f'You choose scissor!{items[user_input]}')
        print(f'system choose = {items[system_choice]}')
        play_ground(user_input,system_choice)
    case 'paper':
        user_input = 2
        print(f'You choose paper!{items[user_input]}')
        print(f'system choose = {items[system_choice]}')
        play_ground(user_input,system_choice)
    case _:
        print("Worng Choice. Please Try Again!")

# 0 > 1 and 2 > 0