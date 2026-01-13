if __name__=="__main__":

    print(r'''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer = input('You are at a crossroad. Where do you want to go?\nType "left" or "right."\n')

if answer == 'left':
    answer = input('You have come to a lake. There is an island in the middle of the lake.\n'
                   'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if answer == 'wait':
        answer = input('You arrive to the island unharmed. There is a house with 3 door.\n'
                       'Type "red" or "yellow" or "blue". Which colour do you choose?\n').lower()
        if answer == 'yellow':
            print("Mission Completed! You found the treasure!")
        elif answer == 'red':
            print("You were burnt by fire!. Game Over!")
        elif answer == 'blue':
            print("You were eaten by beasts! Game Over!")
        else:
            print("You chose a door that doe not exist. Game Over!")
    else:
        print('You were attacked by trout. Game Over!')
        quit()
else:
    print('You fell into a hole. Game Over!')
    quit()