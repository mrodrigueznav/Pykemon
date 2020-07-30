TYPES = [
    "normal",
    "fighting",
    "flying",
    "poison",
    "ground",
    "rock",
    "bug",
    "ghost",
    "steel",
    "fire",
    "water",
    "grass",
    "electric",
    "psychic",
    "ice",
    "dragon",
    "dark",
    "fairy"
    ]

TYPES_CHART =[
    [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,2],
    [1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,1],
    [1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,.5],
    [1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,1],
    [.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,1],
    [1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,1],
    [0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,1],
    [.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,.5],
    [1,1,1,1,2,2,.5,1,.5,.5,2,.5,1,1,.5,1,1,.5],
    [1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1],
    [1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,1],
    [1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,1],
    [1,.5,1,1,1,1,2,2,1,1,1,1,1,.5,1,1,2,1],
    [1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1],
    [1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,2],
    [1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,2],
    [1,.5,1,2,1,1,.5,1,2,1,1,1,1,1,1,0,.5,1]
    ]

WEATHER_MOVES = {
    ""
    "sunny-day": ["harsh-sunlight", "The sunlight turned harsh!"],
    "rain-dance": ["rain", "It started to rain!"],
    "sandstorm": ["sandstorm", "A sandstorm brewed!"],
    "hail": ["hail", "It started to hail!"],
    "shadow-sky": ["shadowy-aura", "A shadowy aurea filled the sky!"]
}
