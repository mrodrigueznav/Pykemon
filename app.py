import random #import rng for battle
import requests
import time
import sys

from battle import *
from pokemon import *

def delay_print(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0)

def createPokemon(pokemonJSON):
    pokemonTypes = []
    pokemonMoves = []
    pokemonStats = []
    for t in pokemonJSON["types"]:
        pokemonTypes.append(t['type']['name'])

    moveList = pokemonJSON['moves']
    random.shuffle(moveList)
    del moveList[4:len(moveList)]
    ix = 0

    for i in moveList:
        moveUrl = moveList[ix]['move']['url']
        getMoveInfo = requests.get(f'{moveUrl}')
        jsonMove = getMoveInfo.json()
        pokemonRandomMoves = {
            'name': moveList[ix]['move']['name'],
            'power': jsonMove['power'],
            'type': jsonMove['type']['name'],
            'damage_class': jsonMove['damage_class']['name']
        }
        pokemonMoves.append(pokemonRandomMoves)
        ix += 1
    
    baseStatList = pokemonJSON['stats']

    for i in baseStatList:
        pokemonTempBaseStats = {
            i['stat']['name']: i['base_stat']            
        }
        pokemonStats.append(pokemonTempBaseStats)

    data = [pokemonTypes, pokemonMoves, pokemonStats]
    return data

def selectAttack(pokemon):
    validAttack = False
    selectedAttack = 0
    while validAttack == False:
        print(f'SELECT ONE ATTACK FOR {pokemon.name}\n')
        for i, x in enumerate(pokemon.moves):
            print(f"{i+1} {x['name']} Power: {x['power']}")
        attackNo = input('Select a move:')
        if attackNo not in ['1','2','3','4']:
            print('Attack must be a number between 1 and 4')
        else:
            selectedAttack = int(attackNo) - 1
            validAttack = True
    return pokemon.moves[selectedAttack]
 
if __name__ == "__main__" :
    apiResponseCode = 0
    while apiResponseCode != 200:
        pokemon1 = input('Select a Pokemon: ')
        getPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon1.lower()}')
        if (getPokemon.status_code != 200):
            print("POKEMON NOT FOUND :(")
        else:
            apiResponseCode = getPokemon.status_code
    jsonPokemon = getPokemon.json()

    rn = random.randint(1,907)
    getSecondPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rn}')
    # getSecondPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/poliwag')
    secondJsonPokemon = getSecondPokemon.json()

    firstPokemonData = createPokemon(jsonPokemon)
    secondPokemonData = createPokemon(secondJsonPokemon)

    Pokemon1 = Pokemon(jsonPokemon['name'], firstPokemonData[0], firstPokemonData[1], firstPokemonData[2])
    Pokemon2 = Pokemon(secondJsonPokemon['name'], secondPokemonData[0], secondPokemonData[1], secondPokemonData[2])

    # Pokemon1.attack(Pokemon2)
    battle = Battle(Pokemon1, Pokemon2)

    while not battle.is_finished():

        turn = Turn()
        turn.command1 = selectAttack(Pokemon1)
        turn.command2 = selectAttack(Pokemon2)

        if turn.can_start():
            battle.manage_turn(turn)
            battle.print_battle_status()