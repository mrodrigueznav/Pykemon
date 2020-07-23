from constants import *
import random

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def manage_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        move1 = 
        move2 = 

        self.pokemon1.current_health -= self.damage_calculation(self.pokemon2, self.pokemon1, move)

    

    def damage_calculation(self, attackingPokemon, targetPokemon, move):
        A, D = 'ATK', 'DEF'
        if move['damage_class'] == 'special':
            A = 'SPATK'
            D = 'SPDEF'
        if move['power'] == None:
            return 0
        atkVsDef = self.stats[A] / targetPokemon.stats[D]
        levelPower = 42 * move['power']
        modifier = self.damageModifiers(move, attackingPokemon, targetPokemon)
        damage = (((levelPower * atkVsDef) / 50) + 2) * modifier
        return round(damage)

    def damageModifiers(self, move, pokemon, targetPokemon):
        targets = 1
        weather = 1
        critical = 1
        critChance = random.random()
        if critChance <= 1/24:
            print('Landed a critical attack')
            critical = 1.5
        randomv = (random.randint(85,100)/100)
        stab = 1
        if move['type'] in pokemon.types:
            stab = 1.5
        attackType = 1
        for t in targetPokemon.types:
            moveTypeIndex = TYPES.index(move['type'])
            targetPokemonTypeIndex = TYPES.index(t)
            typeAdvantage = TYPES_CHART[targetPokemonTypeIndex][moveTypeIndex]
            attackType = attackType * typeAdvantage
        burn = 1
        modifiers = targets * weather * critical * randomv * stab * attackType * burn
        return modifiers