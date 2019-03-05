from random import choice
import json

LUIGI = "Luigi"
MARIO = "Mario"
DK = "DK"
LINK = "Link"
SAMUS = "Samus"
FALCON = "Falcon"
NESS = "Ness"
YOSHI = "Yoshi"
KIRBY = "Kirby"
FOX = "Fox"
PIKA = "Pikachu"
JIGGS = "Jigglypuff"

CHARACTERS = [
    LUIGI, MARIO, DK, LINK, SAMUS, FALCON,
    NESS, YOSHI, KIRBY, FOX, PIKA, JIGGS
]

TOMATO = "MaximTomato"
HEART = "Heart"
STAR = "Star"
SWORD = "BeamSword"
BAT = "HomeRunBat"
FAN = "Fan"
ROD = "StarRod"
GUN = "RayGun"
FIRE = "FireFlower"
HAMMER = "Hammer"
MINE = "MotionSensorBomb"
BOMB = "Bob-omb"
BUMPER = "Bumper"
G_SHELL = "GreenShell"
R_SHELL = "RedShell"
POKEBALL = "Pokeball"


ITEMS = [
    TOMATO, HEART, STAR, SWORD, BAT, FAN, ROD, GUN,
    FIRE, HAMMER, MINE, BOMB, G_SHELL, R_SHELL, POKEBALL
]

WEAPONS = [
    SWORD, BAT, FAN, ROD, GUN,
    FIRE, HAMMER, MINE, BOMB,
    G_SHELL, R_SHELL, POKEBALL
]

HEALING_ITEMS = [
    TOMATO, HEART, STAR
]

CLEFAIRY = "Clefairy"
BEEDRILL = "Beedrill"
CHARIZARD = "Charizard"
SNORLAX = "Snorlax"
CHANCEY = "Chancey"
HITMONLEE = "Hitmonlee"
GOLDEEN = "Goldeen"
MEW = "Mew"
BLASTOISE = "Blastoise"
KOFFING = "Koffing"
MEOWTH = "Meowth"
STARYU = "Staryu"

PKMN = [
    CLEFAIRY, BEEDRILL, CHARIZARD, SNORLAX,
    CHANCEY, HITMONLEE, GOLDEEN, MEW,
    BLASTOISE, KOFFING, MEOWTH, STARYU
]
BONUSES = [
    "Cheap Shot",
    "Mystic or Comet Mystic",
    "DK Defender or DK Perfect",
    "All Variations",
    "Bros Calamity, Kirby Ranks, or Yoshi Rainbow",
    "Fighter Stance",
    "Hawk",
    "Heavy Damage",
    "Item Strike or Item Throw",
    "Judo Warrior or Throw Down",
    "No Damage",
    "No Miss Clear",
    "Pacifist",
    "Pokemon Finish",
    "Shooter",
    "Shield Breaker",
    "Single Move",
    "Special Move",
    "Smash-less"
    "Speed Demon or Speed King",
    "Star Finish",
    "Good Friend or True Friend"
]

STAGE_KILLS = [
    "a Tornado on Hyrule",
    "the Arwing on Sector Z",
    "the Acid onn Planet Zebes",
    "a Pokemon on Saffron City"
]

MEME_MOVES = [
    "Kirby Neutral B",
    "Kirby Up B",
    "Fox Neutral B",
    "DK Neutral B"
    "Yoshi Neutral B",
    "Puff Down B",
    "Luigi Up B",
    "Falcon Neutral B",
    "Pika Down B",
    "Ness Up B"
]

CLASSIC_LEVELS = [
    "Link",
    "Yoshi Team",
    "Fox",
    "Mario Bros",
    "Pikachu",
    "Giant Donkey Kong",
    "Kirby Team",
    "Samus",
    "Metal Mario",
    "Polygon Team",
    "Master Hand"
]

TEMPLATES = {
    "Beat Very Easy (5 Stock) w/ {}, {} or {}": (CHARACTERS, CHARACTERS, CHARACTERS),
    "Beat Normal (3 Stock) w/ {}, {} or {}": (CHARACTERS, CHARACTERS, CHARACTERS),
    "Beat Break the Targets w/ {}, and {}": (CHARACTERS, CHARACTERS),
    "Beat Board the Platforms w/ {}, and {}": (CHARACTERS, CHARACTERS),
    "Beat Break the Targets using only B moves with {}": (CHARACTERS,),
    "Get a {} KO": (WEAPONS,),
    "Use 3 different {}s": (HEALING_ITEMS,),
    "Catch a {} or {}": (PKMN, PKMN),
    "Get a {} bonus": (BONUSES,),
    "Get a stage KO with {}": (STAGE_KILLS,),
    "Defeat {} using only {}": (CLASSIC_LEVELS, MEME_MOVES),
    "Beat Very Easy (5 Stock) with No Continues": (),
    "Beat Normal (3 Stock) with No Continues": (),
    "Beat Very Hard (1 Stock)": ()
}


def fill_depth_1(template, fill):
    output = []

    for item in fill:
        output.append(template.format(item))

    return output


def fill_depth_2(template, fill_a, fill_b):
    output = []
    selections = []

    for a in fill_a:
        selections.append(a)

        for b in fill_b:
            if b not in selections:
                output.append(template.format(a, b))

    return output


def fill_depth_3(template, fill_a, fill_b, fill_c):
    output = []
    selections_a = []

    for a in fill_a:
        selections_a.append(a)
        selections_b = []

        for b in fill_b:
            if b not in selections_a:
                selections_b.append(b)

                for c in fill_c:
                    if c not in selections_b + selections_a:
                        output.append(template.format(a, b, c))

    return output


if __name__ == "__main__":
    goals = {"unique": []}

    for key in TEMPLATES:
        choices = TEMPLATES[key]
        goal_list = []

        if len(choices) == 0:
            goals["unique"].append(key)

        if len(choices) == 1:
            goals[key] = fill_depth_1(key, *choices)

        if len(choices) == 2:
            goals[key] = fill_depth_2(key, *choices)

        if len(choices) == 3:
            goals[key] = fill_depth_3(key, *choices)

    file = open("goal_list.json", "w")
    json.dump(goals, file, indent=4)
    file.close()

