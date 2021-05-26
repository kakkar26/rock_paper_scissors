import untitled2
import random
print('Starting the rock paper scissors game')
player_name = input('Enter your name: ')
print('Pick a hand:(0:Rock,1:Paper,2:Scissors) ')
player_hand = int(input('Please enter a number (0-2): '))
if untitled2.validate(player_hand):

    untitled2.print_all(player_hand, player_name)
    hands = ['Rock', 'Paper', 'Scissors']
    comp_hand = random.randint(0, 2)
    computer_hand = hands[comp_hand]

    print('Computer picked: ' + computer_hand)
    result = untitled2.judge(player_hand, comp_hand)
    print('The result is :' + result)
else:
    print('Enter a valid number')
