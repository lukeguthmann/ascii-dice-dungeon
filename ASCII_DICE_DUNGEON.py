####################################################################
# ASCII BATTLE DUNGEON
##################################################################


print('-' * 60)
print(' ' * 15 + 'ASCII DICE DUNGEON')
print('-' * 60)

import random
import time

def adding_enemies():

    ''' empty dictionary for enemy holding and player chooses enemy count '''

    enemies_values_dictionary = {}

    while True:
        try:
            how_many_enemies_in_the_game_player_chooses = int(input('how many enemies would you like in the game?'))
            break
        except:
            print('please enter an integer for number of enemies \n')

    for enemy in range(how_many_enemies_in_the_game_player_chooses):
        random_name = (random.sample('abcdefghijklmopqrstuvwxyz', 3))
        new_name = ''.join(random_name)
        enemies_values_dictionary[f'enemy_{new_name}'] = random.randint(1, 6)

    enemy_count = (len(enemies_values_dictionary))
    print(f'the total enemy count is {enemy_count}')
    return enemies_values_dictionary

adding_enemy_values = (adding_enemies())


def time_delay():

    ''' time delay for aesthetics'''

    delay_message = "Generating enemies"
    for x in range(0, 3):
        delay_message = (delay_message + '.')
        time.sleep(0.7)
        print(delay_message)
    print(f'Generated enemies: {adding_enemy_values}')

time_delay()


def battle_screen_function(stored_enemies_dictionary):

    ''' the battle screen for enemies and hero '''
    battle_screen_enemies = len(stored_enemies_dictionary.keys())
    battle_field_print = []

    for adding_enemy_to_screen in range(battle_screen_enemies):
        battle_field_print.append("- - - [enemy]")


    battle_field_print.insert(0, '( •_•)>|--->')
    print(f' // The battle field has {len(battle_field_print) - 1} enemies')
    print(*battle_field_print)
    print('-' * 40)
    return battle_field_print

battle_screen_returned = battle_screen_function(adding_enemy_values)


def players_total_health():

    '''player choosing health and using ▲ as per chosen health'''

    while True:
        try:
            players_health = int(input('How many health points would you like?'))
            break
        except:
            print('sorry, please enter an integer for players health \n')

    print(f'the health of your player is {players_health} health points')
    print(f'Your health ({players_health}): ', ('▲ ' * players_health))
    print('-' * 40)
    stats = range(0, players_health)

    return players_health

players_health_returned_value_var = players_total_health()


def battle_system(players_health_returned_var_imported):

    '''the battle system - if a players rolls greater than or equal to enemies health,
        players wins, enemy defeaterd. Otherwise, player loses'''

    for fight_enemy_name, fight_enemy_health in adding_enemy_values.items():
        while fight_enemy_health:
            roll_the_dice = input(
                '> > > > [NEXT ROUND] - PRESS ANY BUTTON TO ROLL BATTLE DICE\n')
            players_attack_roll = random.randint(1, 6)

            if players_health_returned_var_imported == 0:
                return exit('GAME OVER . . .  YOU HAVE NO HEALTH LEFT')

            elif players_attack_roll >= fight_enemy_health:
                print(f'you rolled an ATTACK of {players_attack_roll}')

                print(" ^^^^ ENEMY DEFEATED")
                battle_screen_returned.insert(1, f'- - - [lvl {fight_enemy_health} enemy defeated]')
                battle_screen_returned.remove('- - - [enemy]')
                print(*battle_screen_returned)
                print(f'Your health ({players_health_returned_var_imported}): ',
                      ('▲ ' * players_health_returned_var_imported))
                print('-' * 40)

                break

            elif players_attack_roll < fight_enemy_health:
                print(f'you rolled an ATTACK of {players_attack_roll}')

                players_health_returned_var_imported -= 1
                print('!!!! the enemy HIT YOU leaving you with {} health points'.format(players_health_returned_var_imported))
                print('( X_x)> ')
                print(f'Your health ({players_health_returned_var_imported}): ',
                      ('▲ ' * players_health_returned_var_imported))
                print('-' * 40)

battle_system(players_health_returned_value_var)

exit('YOU WON! Thank you for playing ASCII DICE DUNGEON')



