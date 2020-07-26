from constants import *
import random

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.current_weather = None
        self.current_weather_turn_left = 0
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
        print(f"{self.pokemon1.name} used {command1['name']}")
        self.pokemon2.current_health -= self.damage_calculation(self.pokemon1, self.pokemon2, command1)
        self.is_finished()
        print(f"{self.pokemon2.name} used {command2['name']}")
        self.pokemon1.current_health -= self.damage_calculation(self.pokemon2, self.pokemon1, command2)
        self.is_finished()
        self.endTurnDamage(self.pokemon1)
        self.endTurnDamage(self.pokemon2)
        self.actual_turn += 1
        self.current_weather_turn_left = self.manage_weather_turnleft(self.current_weather_turn_left)

    def manage_weather_turnleft(self, current_weather_turn_left):
        if current_weather_turn_left > 0:
            current_weather_turn_left -= 1
        if current_weather_turn_left == 0:
            print('The weather is clear')
        return current_weather_turn_left
    
    def print_battle_status(self):
        print(f"{self.pokemon1.name} has {self.pokemon1.current_health} left!")
        print(f"{self.pokemon2.name} has {self.pokemon2.current_health} left!")


    def damage_calculation(self, attackingPokemon, targetPokemon, move):
        if move['power'] == None:
            self.current_weather = self.setWeather(self.current_weather, move)
            return 0
        A, D = 'ATK', 'DEF'
        if move['damage_class'] == 'special':
            A = 'SPATK'
            D = 'SPDEF'
        atkVsDef = attackingPokemon.stats[A] / targetPokemon.stats[D]
        levelPower = 42 * move['power']
        modifier = self.damageModifiers(move, attackingPokemon, targetPokemon)
        damage = (((levelPower * atkVsDef) / 50) + 2) * modifier
        print(f"{attackingPokemon.name} has dealt {round(damage)} to {targetPokemon.name}")
        return round(damage)

    def endTurnDamage(self, pokemon):
        damage = 0
        WEATHER_EFFECTS = {
            'hail': [['ice'], .0625],
            'sandstorm': [['ground', 'rock', 'steel'], .0625]
        }
        invulnerable = any(t in pokemon.types for t in WEATHER_EFFECTS[self.current_weather][0])
        if not invulnerable:
            damage = pokemon.current_health *  WEATHER_EFFECTS[self.current_weather][1]
            print(f'{pokemon.name} receives {round(damage)} from {self.current_weather}')      
        return round(damage)

    def damageModifiers(self, move, pokemon, targetPokemon):
        targets = 1
        weather = 1
        if  (self.current_weather == 'harsh-sunlight' and move['type'] == 'fire') | \
            (self.current_weather == 'rain' and move['type'] == 'water') :
            weather = 1.5
        elif    (self.current_weather == 'harsh-sunlight' and move['type'] == 'water') | \
                (self.current_weather == 'rain' and move['type'] == 'fire') :
                weather = .5
        print(f'current weather: {self.current_weather}, weather: {weather}')
        critical = 1
        if random.random() <= 1/24:
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

    def setWeather(self, current_weather, move):
        if move['name'] in WEATHER_MOVES:            
            next_weather = WEATHER_MOVES[move['name']][0]
            if current_weather == next_weather:
                print(f"{move['name']} has failed!")
            else:
                print(f"{WEATHER_MOVES[move['name']][1]}")
                self.current_weather_turn_left = 6
                return next_weather
        return current_weather

class Turn:

    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):       
        return self.command1 is not None and self.command2 is not None