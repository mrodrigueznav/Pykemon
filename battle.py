from constants import *
import random

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.current_weather = None
        self.actual_turn = 0

    def is_finished(self):
        finished = self.pokemon1.current_health <= 0 or self.pokemon2.current_health <= 0
        if finished:
            self.print_winner()
        return finished
    
    def print_winner(self):
        if self.pokemon1.current_health <= 0 < self.pokemon2.current_health:
            print(f'{self.pokemon2.name} won')
        if self.pokemon2.current_health <= 0 < self.pokemon1.current_health:
            print(f'{self.pokemon1.name} won')
        else:
            print('Empate')

    def manage_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        self.pokemon1.current_health -= self.damage_calculation(self.pokemon2, self.pokemon1, command2)
        self.pokemon2.current_health -= self.damage_calculation(self.pokemon1, self.pokemon2, command1)
        self.actual_turn += 1
    
    def print_battle_status(self):
        print(f"{self.pokemon1.name} has {self.pokemon1.current_health} left!")
        print(f"{self.pokemon2.name} has {self.pokemon2.current_health} left!")


    def damage_calculation(self, attackingPokemon, targetPokemon, move):
        A, D = 'ATK', 'DEF'
        if move['damage_class'] == 'special':
            A = 'SPATK'
            D = 'SPDEF'
        if move['power'] == None:
            return 0
        atkVsDef = attackingPokemon.stats[A] / targetPokemon.stats[D]
        levelPower = 42 * move['power']
        modifier = self.damageModifiers(move, attackingPokemon, targetPokemon)
        damage = (((levelPower * atkVsDef) / 50) + 2) * modifier
        print(f"{attackingPokemon.name} has dealt {round(damage)} to {targetPokemon.name}")
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
            print('STAB Attack')
            stab = 1.5
        attackType = 1
        for t in targetPokemon.types:
            moveTypeIndex = TYPES.index(move['type'])
            targetPokemonTypeIndex = TYPES.index(t)
            typeAdvantage = TYPES_CHART[targetPokemonTypeIndex][moveTypeIndex]
            attackType = attackType * typeAdvantage
        if attackType > 1:
            print("It's super effective!")
        burn = 1
        modifiers = targets * weather * critical * randomv * stab * attackType * burn
        return modifiers

class Turn:

    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):       
        return self.command1 is not None and self.command2 is not None