import random
import logo

head_tail = [logo.head_logo,logo.tail_logo]
user_guess = int(input("Guess head or tail (0 for head and tail for 1) : "))
system_choice = random.randint(0,1)
print(head_tail[user_guess])
print(f"Your choice is {head_tail[user_guess]}")

if user_guess == system_choice:
    print(f"You Win!The Result is{head_tail[system_choice]}")
else:
    print(f"You loose!The Result is {head_tail[system_choice]}")