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
        iv = [random.randint(1,31),31,31,31,31,31]
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
            'HP': ((((2*baseStats['HP'])+iv[0])*level)/100)+level+10,
            'ATK': ((((2*baseStats['ATK'])+iv[1])*level)/100)+5,
            'DEF': ((((2*baseStats['DEF'])+iv[2])*level)/100)+5,
            'SPATK': ((((2*baseStats['SPATK'])+iv[3])*level)/100)+5,
            'SPDEF': ((((2*baseStats['SPDEF'])+iv[4])*level)/100)+5,
            'SPD': ((((2*baseStats['SPD'])+iv[5])*level)/100)+5,
        }
        return stats
