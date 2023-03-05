import random
option = ('rock', 'scissor', 'paper')
user_option = input("Choose between: rock, scissor or paper. Your option is ").lower()
computer_option = random.choice(option)
print('user_option => ',user_option)
print('computer_option => ',computer_option)
if not user_option in option:
    print('Type a right option')

if user_option == computer_option:
    print("No body win")
elif user_option == 'rock' and computer_option == 'paper':
    print('you lost')
elif user_option == 'rock' and computer_option == 'scissor':
    print('you win')
elif user_option == 'paper' and computer_option == 'rock':
    print('you win')
elif user_option == 'paper' and computer_option == 'scissor':
    print('you lost')
elif user_option == 'scissor' and computer_option == 'paper':
    print('you win')
elif user_option == 'scissor' and computer_option == 'rock':
    print('you lost')