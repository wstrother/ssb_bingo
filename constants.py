# all the characters

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

# all the items

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

# all the 1P Mode bonuses

BONUSES = [
    "Cheap Shot",
    "Mystic or Comet Mystic",
    "DK Defender or DK Perfect",
    "Bros Calamity, Kirby Ranks, or Yoshi Rainbow",
    "Fighter Stance",
    "Hawk",
    "Heavy Damage",
    "Judo Warrior or Throw Down",
    "No Damage",
    "No Miss Clear",
    "Pacifist",
    "Pokemon Finish",
    "Shooter",
    "Special Move",
    "Smash-less or Smash-mania",
    "Speed Demon or Speed King",
    "Star Finish",
    "Good Friend or True Friend"
]

# all the stage kills

STAGE_KILLS = [
    "a Tornado on Hyrule",
    "the Arwing on Sector Z",
    "the Acid on Planet Zebes",
    "a Pokemon on Saffron City"
]

# meme moves

MEME_MOVES = [
    "Kirby Neutral B",
    "Kirby Up B",
    "Fox Neutral B",
    "DK Neutral B",
    "Yoshi Neutral B",
    "Puff Down B",
    "Luigi Up B",
    "Falcon Neutral B",
    "Pika Down B",
    "Ness Up B"
]

# 1P levels

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

# goal templates and unique goals

BEAT_VE_CHOICE = "Beat Very Easy (5 Stock) w/ {}, {}, and {}"
BEAT_N_CHOICE = "Beat Normal (3 Stock) w/ {} and {}"
BEAT_VH_CHOICE = "Beat Very Hard (1 Stock) w/ {}"
BTT_CHOICE = "Beat Break the Targets w/ {}, {}, and {}"
BTP_CHOICE = "Beat Board the Platforms w/ {}, {}, and {}"
BTT_B_MOVE = "Beat Break the Targets using only B moves with {}"
WPN_KO = "Get a KO with the {}"
HEAL_3 = "Use 3 different {}s (in 1P Game or VS Mode)"
PKMN_CATCH = "Catch a {} or {}"
BONUS = "Get the {} bonus"
STAGE_KO = "Get a stage KO with {}"
MEME_KO = "Defeat {} (in 1P Game) using only {}"
BTP_FAST = "Beat Board the Platforms in under 1 minute w/ {}"
BTT_FAST = "Beat Break the Targets in under 1 minute w/ {}"
UNIQUE_KEY = "unique"

UNIQUE = [
    "Beat Very Easy (5 Stock) with No Continues",
    "Beat Normal (3 Stock) with No Continues",
    "Beat Very Hard (1 Stock)",
    "SD on Board the Platforms with every character",
    "SD on Break the Targets with every character",
    "Spike an opponent through the acid on Planet Zebes",
    "Complete 6 different Break the Targets stages",
    "Complete 6 different Board the Platforms stages",
    "Catch a Mew",
    "Break an opponent's shield",
    "Win a 1 v 3 against Level 9 CPUs"
]

TEMPLATES = {
    BEAT_VE_CHOICE: (CHARACTERS, CHARACTERS, CHARACTERS),
    BEAT_N_CHOICE: (CHARACTERS, CHARACTERS),
    BEAT_VH_CHOICE: (CHARACTERS,),
    BTT_CHOICE: (CHARACTERS, CHARACTERS, CHARACTERS),
    BTP_CHOICE: (CHARACTERS, CHARACTERS, CHARACTERS),
    BTP_FAST: (CHARACTERS,),
    BTT_FAST: (CHARACTERS,),
    BTT_B_MOVE: (CHARACTERS,),
    WPN_KO: (WEAPONS,),
    HEAL_3: (HEALING_ITEMS,),
    PKMN_CATCH: (PKMN, PKMN),
    BONUS: (BONUSES,),
    STAGE_KO: (STAGE_KILLS,),
    MEME_KO: (CLASSIC_LEVELS, MEME_MOVES),
}
