import random
from constants import *
from app import delay_print

class Pokemon:
    def __init__(self, name, types, moves, stats):
        self.name = name
        self.types = types
        self.moves = moves
        self.stats = self.getStats(stats)
        self.current_health = self.stats['HP']

    #Regresar a mejorar esto con filter
    def getStats(self, stats):
        iv = 31
        level = 100
        baseStats = {
            'HP': stats[0]['hp'],
            'ATK': stats[1]['attack'],
            'DEF': stats[2]['defense'],
            'SPATK': stats[3]['special-attack'],
            'SPDEF': stats[4]['special-defense'],
            'SPD': stats[5]['speed']
        }

        stats = {
            'HP': ((((2*baseStats['HP'])+iv)*level)/100)+level+10,
            'ATK': ((((2*baseStats['HP'])+iv)*level)/100)+5,
            'DEF': ((((2*baseStats['HP'])+iv)*level)/100)+5,
            'SPATK': ((((2*baseStats['HP'])+iv)*level)/100)+5,
            'SPDEF': ((((2*baseStats['HP'])+iv)*level)/100)+5,
            'SPD': ((((2*baseStats['HP'])+iv)*level)/100)+5,
        }
        return stats

    def attack(self, targetPokemon):
        print("Comienzan los putazos")
        print(f"{self.name}")
        print("TYPES", self.types)
        print("ATK", self.stats["ATK"])
        print("DEF", self.stats["DEF"])

        while (self.health > 0) and (targetPokemon.health > 0):
            pokemonAttack = selectAttack(self.moves)

            delay_print(f"{self.name} used {self.moves[pokemonAttack]['name']} on {targetPokemon.name} \n")
            damageModifier = self.damageModifiers(self.moves[pokemonAttack], self, targetPokemon)
            damageDealt = self.damage(targetPokemon, self.moves[pokemonAttack], damageModifier)
            targetPokemon.health = targetPokemon.health - damageDealt
            print(f'{self.name} dealt {damageDealt} damage to {targetPokemon.name}')
            if (targetPokemon.health <= 0):
                print(f'{targetPokemon.name} fainted.')
                print(f'{self.name} wins.')
                break
            else:
                print(f'{targetPokemon.name} health is now {targetPokemon.health}')

            print(f'Go {targetPokemon.name}')

            targetPokemonAttack = selectAttack(targetPokemon.moves)
            
            delay_print(f"{targetPokemon.name} used {targetPokemon.moves[targetPokemonAttack]['name']} on {self.name} \n")
            damageModifier = self.damageModifiers(targetPokemon.moves[pokemonAttack], targetPokemon, self)
            damageDealt = targetPokemon.damage(self, targetPokemon.moves[targetPokemonAttack], damageModifier)
            self.current_health = self.current_health - damageDealt
            print(f'{targetPokemon.name} dealt {damageDealt} damage to {self.name}')
            if (self.health <= 0):
                print(f'{self.name} fainted.')
                print(f'{targetPokemon.name} wins.')
                break
            else:
                print(f'{self.name} health is now {self.health}')
