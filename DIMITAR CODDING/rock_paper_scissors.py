import random

first_player = input('Ти си на ход:(rock, paper, scissors): ')
possible_actions = ['rock', 'paper', 'scissors']
computer = random.choice(possible_actions)
print(f'Ти избираш {first_player}, компютъра избира {computer}.\n')

if first_player == computer:
    print(f'И двамата играчи избраха {first_player}. Имаме равенство!')
elif first_player == "rock":
    if computer == "scissors":
        print('Камъка счупи ножицата! Ти спечели!')
    else:
        print('Хартията покрива камъка! Ти загуби!')
elif first_player == "paper":
    if computer == "rock":
        print('Хартията покрива камъка! Ти спечели!')
    else:
        print('Ножицата реже хартията! Ти загуби!')
elif first_player == "scissors":
    if computer == "paper":
        print('Ножицата реже хартията! Ти спечели!')
    else:
        print('Камъка счупи ножицата! Ти загуби')