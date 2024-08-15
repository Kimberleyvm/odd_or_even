import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = random.choice([rock, paper, scissors])

user = int(input('What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors:\n'))
if user == 0:
    print('You chose: ', rock, 'The computer chose: ', game)
    if game is paper:
        print('You lose.')
    elif game is scissors:
        print('You win!')
    else:
        print('Equal!')
elif user == 1:
    print('You chose: ', paper, 'The computer chose: ', game)
    if game is scissors:
        print('You lose.')
    elif game is rock:
        print('You win!')
    else:
        print('Equal!')
elif user == 2:
    print('You chose: ', scissors, 'The computer chose: ', game)
    if game is paper:
        print('You win!')
    elif game is rock:
        print('You lose')
    else:
        print('Equal!')
else:
    print('wrong input. please try again!')
