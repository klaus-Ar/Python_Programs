# This program is about creating a simple game
# It's actually not a game
# The player will have 500 Health initially

import random

playerhp = 500

while playerhp == 500:
    attack = input("'s' to attack and 'e' to end and 'c' to continue the attack.!:  ")
    enemy_attack = random.randrange(0, 500)
    health = playerhp - enemy_attack

    if attack == 's' or attack == 'c':
        if health >=30:
            print("The player loses %d HP! His current Health has %d points..!"%(enemy_attack, health))
            continue
        if health <= 30:
             print('''
                    You are saved by our Holy Father.!
                    Drink some water from the Holy fountain to regain the health.!
                    Lucifer will taker care of the bad guys :-)
                    ''')
             break
        else:
             continue
    elif attack == 'e':
        print('''
            Thank you for playing this game.!
            Have a bright day!!!
            ''')
        break
    else:
        print('''
            Invalid Entry!    :-(
            Please check the entered data:
            ''')



