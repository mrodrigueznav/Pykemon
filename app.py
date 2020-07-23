import random #import rng for battle
import battle
import requests
import time
import sys

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

    def selectAttack(moves):
        validAttack = False
        selectedAttack = 0
        while validAttack == False:
            print('SELECT ONE ATTACK\n')
            for i, x in enumerate(moves):
                print(f"{i+1} {x['name']} Power: {x['power']}")
            attackNo = input('Select a move:')
            if attackNo not in ['1','2','3','4']:
                print('Attack must be a number between 1 and 4')
            else:
                selectedAttack = int(attackNo) - 1
                validAttack = True
        return selectedAttack
 
if __name__ == "__main__" :
    # theApp = App()
    # theApp.on_execute()
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
    # getSecondPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rn}')
    getSecondPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/3')
    secondJsonPokemon = getSecondPokemon.json()

    firstPokemonData = createPokemon(jsonPokemon)
    secondPokemonData = createPokemon(secondJsonPokemon)

    Pokemon1 = Pokemon(jsonPokemon['name'], firstPokemonData[0], firstPokemonData[1], firstPokemonData[2])
    Pokemon2 = Pokemon(secondJsonPokemon['name'], secondPokemonData[0], secondPokemonData[1], secondPokemonData[2])

    # Blastoise = Pokemon('Blastoise',
    # ['Water'], ['Scald', 'Rapid Spin', 'Ice Beam', 'Toxic'],
    # {'HP': 299, 'ATK': 181, 'DEF': 259, 'SPATK': 206, 'SPDEF': 246, 'SPD': 192})
    # battle.start(Pokemon1, Pokemon2)
    Pokemon1.attack(Pokemon2)
