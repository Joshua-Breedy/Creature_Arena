# random integer input
from random import randint

# boolean used to keep the game running until the warrior quits
game_running = True
# List to store results after a game is finished
game_results = []
# Counts the number of rounds played against previous creature to use the special attack
round_counter = [0]
# Shows how many creatures killed as a stat
creatures_killed = []


# random value in range that calculates the creature's attack damage in a particular round
def calculate_creature_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


# random value in range that calculates the warrior's attack damage in a particular round
def calculate_warrior_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


# prints whoever has won the game, either the warrior or the creature
def game_ends(winner_name):
    print(f'{winner_name} won the game')


# Sets the creature's name
def creature_names(x):
    creature_name = ["Duskfang", "Slagchild", "Dawnseeker", "Foulthing"]
    return creature_name[x]


# Sets the creature's attack minimum value
def creature_attack_min(x):
    attack_min = [10, 12, 15, 17]
    return attack_min[x]


# Sets the creature's attack maximum value
def creature_attack_max(x):
    attack_max = [15, 15, 20, 20]
    return attack_max[x]


# Sets the creature's health
def creature_health(x):
    health = [150, 200, 250, 300]
    return health[x]


# Sets the creature's description
def creature_description(x):
    creature_descript = ['An 8 foot tall creature, a Duskfang is all black and posesses genetics from both a duck and '
                         '\nbat. A Duskfang\'s special attack is The Whirl, can flap its wings in a whirlwind position '
                         '\nto attack a player.',
                         'A Slagchild is a transparent wolf-like creature with 2 heads that possesses a Superbite '
                         '\nattack. Using superbite it can attack an enemy from up to 20 feet away.',
                         'The Dawnseeker is one of the feared creatures in the land, with it possesses the Seeker '
                         '\nspecial attack to smell and attack a person from a mile away. A cross between a bloodhound '
                         '\nand a jaguar, a dawnseeker has mastered hunting and stealth',
                         'A Foulthing is a mud-based creature that releases a liquid that causes burns and rashes on '
                         '\nan opponent\'s skin. It\'s specialty is shapeshifting into the ground, locking and sticking'
                         '\n an enemy in place.']
    return creature_descript[x]


# Sets the attributes for a new creature that appears after the previous one has died
def creature_change(x):
    creature['name'] = creature_names(x)
    creature['health'] = creature_health(x)
    creature['attack_min'] = creature_attack_min(x)
    creature['attack_max'] = creature_attack_max(x)
    creature['description'] = creature_description(x)


# Sets the attributes for the final boss creature
def creature_boss():
    creature['name'] = 'Ender'
    creature['health'] = 500
    creature['attack_min'] = 20
    creature['attack_max'] = 40
    creature['description'] = 'A faceless large green worm-like creature, the Ender measures 60 feet in length. ' \
                              '\nEquipped with a snake-like tongue, the Ender is covered in a spikey outer shell that ' \
                              '\ncan pierce flesh. It\'s special attack is the Blitz, where it can shoot up and around ' \
                              '\nan enemy at 50 mph. '


# Function to go to the next level, uses the round counter value and the random integer x value
def next_level(counter, x):
    # if the current creature dies and the amount of rounds played is less than 30, then bring the next creature in
    if creature['health'] <= 0 and gen_counter < 30:
        round_counter.append(counter)
        creature_change(x)
        print('A new creature approaches! Their name is ' + creature['name'])
        warrior_stats_improve()
    # if the current creature dies and the amount of rounds played is more than 30, either the warrior has won or the
    # boss needs to be brought in
    elif creature['health'] <= 0 and gen_counter > 30:
        # checks if the creature is the boss and if not the boss is sent in
        if creature['name'] != 'Ender':
            creature_boss()
            warrior_stats_improve()
        # if the creature is boss and has died, the warrior has won
        else:
            warrior_won = True


# Increases the warrior's attributes when a new creature is brought in
def warrior_stats_improve():
    warrior['health'] = default_health + (30 * len(creatures_killed))
    warrior['heal'] += 2
    warrior['attack_max'] += 8
    warrior['attack_min'] += 8


print("WELCOME TO CREATURE ARENA!")

# while loop that exits when the game stops running
while game_running:
    # counts the rounds for the current creature
    counter = 0
    # counts the rounds for all creature fought
    gen_counter = 0
    # number of heals allowed for the warrior per creature
    heals = 5
    # sets the boolean value of new round to true
    new_round = True
    # the initial health value of the warrior is set
    default_health = 100
    # used to count special attacks (maximum is 3 per creature)
    special_attack_counter = 0
    # sets the default values for the warrior in a dictionary
    warrior = {'name': 'warrior', 'attack_min': 15, 'attack_max': 17, 'heal': 16, 'health': 100, 'heals_left': heals}
    # if it is the first round, send out the default creature(Anglefin)
    if gen_counter == 0:
        creature = {'name': 'Anglefin', 'attack_min': 5, 'attack_max': 10,
                    'health': 100, 'description': 'A large toad-like creature, an Anglefin oddly possesses a large '
                                                  '\ndorsal fin that shoots out darts as a defense mechanism. It\'s '
                                                  '\nspecial attack is the Sonic Croak, which can cause dizziness, '
                                                  '\npopped eardrums, and shattered glass'}
    # if the first creature has died, set the next creature's values
    else:
        creature = {'name': creature_names(x), 'attack_min': creature_attack_min(x),
                    'attack_max': creature_attack_max(x),
                    'health': creature_health(x)}

    print('---' * 7)
    print('Enter Your Warrior\'s Name')
    # asks for user input and use it to set input name
    warrior['name'] = input()
    # prints out the warrior's and the creature's name and health
    print(warrior['name'])
    print('Health: ' + str(warrior['health']))
    print(creature['name'])
    print('Health: ' + str(creature['health']))
    # sets the first creature's health
    initial_creature_health = creature['health']
    # while loop that starts the new round and ends when either the warrior or the creature wins
    while new_round:
        # random value used to set the creature's attribute
        x = randint(0, 3)
        # boolean value that checks if either the warrior or the creature has won
        warrior_won = False
        creature_won = False

        # Prints out the user's options
        print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Special Attack')
        print('D) Monster Description')
        print('X) Exit Game')
        # displays these options if a player has already played before
        if len(game_results) != 0:
            print('Y) Show Results')
        # displays these options if there is a creature already killed
        if len(creatures_killed) != 0:
            print('A) Show Creatures Killed')
        print('---' * 7)
        # sets whatever the user inputs to uppercase lettering
        warrior_choice = input().upper()

        # sets actions if the user choices '1' as an option
        if warrior_choice == '1':
            # increases round counter by one
            counter += 1
            # sets creature's health after the warrior attacks
            creature['health'] = creature['health'] - calculate_warrior_attack(warrior['attack_min'],
                                                                               warrior['attack_max'])
            # if the creature and warrior has health left, the monster can attack
            if creature['health'] >= 0 and warrior['health'] >= 0:
                warrior['health'] = warrior['health'] - calculate_creature_attack(creature['attack_min'],
                                                                                  creature['attack_max'])
            # if warrior has no health points left, the creature has won the game
            elif warrior['health'] <= 0:
                game_ends(creature['name'])
                creature_won = True
            # if the creature has no health points left and is not the boss, the elif statement is triggered
            elif creature['health'] <= 0 and creature['name'] != 'Ender':
                # adds creature to creatures killed list
                creatures_killed.append(creature['name'])
                # calls the next level function
                next_level(counter, x)
                # adds rounds for this creature to the overall counter
                gen_counter += counter
                # resets counter
                counter = 0
                # resets special attack counter
                special_attack_counter = 0
                # resets warrior's heals left
                warrior['heals_left'] = 5
            # if the creature has no health points left and is not the boss, then the warrior has won
            elif creature['health'] <= 0 and creature['name'] == 'Ender':
                warrior_won = True
        # sets actions if the user choices '2' as an option
        elif warrior_choice == '2':
            # if statement that triggers if there are any heals left
            if heals > 0:
                # increases round counter by one
                counter += 1
                # reduces heals left by one
                warrior['heals_left'] -= 1
                # adds heal amount to the warrior's health
                warrior['health'] = warrior['health'] + warrior['heal']
                # the warrior's health decreases because the creature is able to attack as the player heals
                warrior['health'] = warrior['health'] - calculate_creature_attack(creature['attack_min'],
                                                                                  creature['attack_max'])
                # if the warrior has no health points left after, the creature has won
                if warrior['health'] <= 0:
                    game_ends(creature['name'])
                    creature_won = True
            # if there is no heals left, print statement
            else:
                print('No heals left')
        # sets actions if the user choices '3' as an option
        elif warrior_choice == '3':
            # increases round counter by one
            counter += 1
            # if the previous monster's rounds are less than 12 but greater than 0, the special attack can be used
            if 12 > round_counter[-1] > 0 and special_attack_counter < 3:
                # creature's health is the creature's health minus the warrior's attack which is doubled as a special
                # move
                creature['health'] = creature['health'] - (
                        calculate_warrior_attack(warrior['attack_min'], warrior['attack_max']) * 2)
                warrior['health'] = int(warrior['health'] - (
                        calculate_creature_attack(creature['attack_min'], creature['attack_max']) / 2))
                special_attack_counter += 1
                # if the creature has no health points and is not the boss, if statement occurs
                if creature['health'] <= 0 and creature['name'] != 'Ender':
                    # adds creature to creatures killed list
                    creatures_killed.append(creature['name'])
                    # calls the next level function
                    next_level(counter, x)
                    # adds rounds for this creature to the overall counter
                    gen_counter += counter
                    # resets counter
                    counter = 0
                    # resets special attack counter
                    special_attack_counter = 0
                # if the creature has no health points and is the boss, the warrior has won
                elif creature['health'] <= 0 and creature['name'] == 'Ender':
                    warrior_won = True
            # runs else if the last creature was no defeated in less than 12 rounds or there was no previous creature
            elif round_counter[-1] > 12 or round_counter[-1] == 0:
                print("Only available after the last creature has been defeated before 12 rounds")
            # removes round counted and executes if three special moves have already been used
            else:
                counter -= 1
                print("Only three special moves can be used per creature")
        elif warrior_choice == 'D':
            print(creature['description'])
        # sets actions if the user choices 'X' as an option
        elif warrior_choice == 'X':
            # exits the game
            new_round = False
            game_running = False
        # sets actions if the user choices 'Y' as an option
        elif warrior_choice == 'Y':
            # prints stats in game_results list if there is anything in game_results
            if game_results is None:
                for stat in game_results:
                    print(stat)
            # prints invalid input if there is nothing in game_results
            else:
                print('Invalid Input')
        # sets actions if the user choices 'A' as an option
        elif warrior_choice == 'A':
            # prints stats in creatures_killed list if there is anything in creatures_killed
            if creatures_killed is None:
                for names in creatures_killed:
                    print(names)
            # prints invalid input if there is nothing in game_results
            else:
                print('Invalid Input')
        # if player inputs value that is not an option, print statement
        else:
            print('Invalid Input')
        # prints stats while the warrior and creature is still battling
        if warrior_won == False and creature_won == False:
            print(warrior['name'])
            print('Health: ' + str(warrior['health']))
            print('Heals left: ' + str(warrior['heals_left']))
            print(creature['name'])
            print('Health: ' + str(creature['health']))
        # else if statement that saves results and stops the round if the warrior wins
        elif warrior_won:
            game_ends(warrior['name'])
            round_result = {'name': warrior['name'], 'health': warrior['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
        # else if statement that saves results and stops the round if the warrior wins
        elif creature_won:
            creatures_killed.clear()
            round_result = {'name': warrior['name'], 'health': warrior['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
