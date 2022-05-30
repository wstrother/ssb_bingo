// game constants

const CHARACTERS = [
    "Luigi", "Mario", "Donkey Kong", "Link", "Samus", "Captain Falcon",
    "Ness", "Yoshi", "Fox", "Kirby", "Pikachu", "Jigglypuff"
];

const ITEMS = {
    "all": [
        "MaximTomato",
        "Heart",
        "Star",
        "BeamSword",
        "HomeRunBat",
        "Fan",
        "StarRod",
        "RayGun",
        "FireFlower",
        "Hammer",
        "MotionSensorBomb",
        "Bob-omb",
        "Bumper",
        "GreenShell",
        "RedShell",
        "Pokeball"
    ],
    "weapons": [
        "BeamSword", "HomeRunBat", "Fan", "StarRod", "RayGun", "FireFlower",
        "Hammer", "MotionSensorBomb", "Bob-omb", "Bumper", "GreenShell",
        "RedShell", "Pokeball"
    ],
    "healing_items": [
        "MaximTomato", "Heart", "Star"
    ]
};

const POKEMON = [
    "Clefairy",
    "Beedrill",
    "Charizard",
    "Snorlax",
    "Chancey",
    "Hitmonlee",
    "Goldeen",
    "Blastoise",
    "Koffing",
    "Meowth",
    "Staryu"
]

const BONUSES = [
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
];

const STAGE_KILLS = [
    "a Tornado on Hyrule",
    "the Arwing on Sector Z",
    "the Acid on Planet Zebes",
    "a Pokemon on Saffron City"
];

const MEME_MOVES = [
    "Kirby Neutral B",
    "Kirby Up B",
    "DK Neutral B",
    "Yoshi Neutral B",
    "Puff Down B",
    "Luigi Up B",
    "Falcon Neutral B",
    "Pika Down B",
    "Ness Up B"
];

const CLASSIC_LEVELS = [
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
];


// goal templates

const GOALS = {
    "templates": {
        "bonus_games": {
            "BTT_CHOICE": ["Beat Break the Targets w/ {}, {}, and {}", CHARACTERS], 
            "BTP_CHOICE": ["Beat Board the Platforms w/ {}, {}, and {}", CHARACTERS],
            "BTT_B_MOVE": ["Beat Break the Targets using only B moves with {}", CHARACTERS],
            "BONUS_BOTH": ["Beat Both Bonus Games w/ {}", CHARACTERS],
        },
        "1p_mode": {
            "BEAT_VE_CHOICE": ["Beat Very Easy (5 Stock) w/ {}, {}, and {}", CHARACTERS],
            "BEAT_N_CHOICE": ["Beat Normal (3 Stock) w/ {} and {}", CHARACTERS],
            "BEAT_VH_CHOICE": ["Beat Very Hard (1 Stock) w/ {}", CHARACTERS],
        },
        "rng": {
            "WPN_KO": ["Get a KO (in 1P Game) with the {}", ITEMS['weapons']],
            "HEAL_3": ["Use 3 different {}s (in 1P Game)", ITEMS['healing_items']],
            "PKMN_CATCH": ["Catch a {} or {} (in 1P Game)", POKEMON],
            "STAGE_KO": ["Get a stage KO with {}", STAGE_KILLS],
        },
        "other": {
            "GET_BONUS": ["Get the {} Bonus", BONUSES],
            "MEME_KO": ["Defeat {} (in 1P Game) using only {}", CLASSIC_LEVELS, CHARACTERS]
        }
    },
    "unique": {
        "bonus_games": {
            "BTP_SD": "SD on Board the Platforms with every character",
            "BTT_SD": "SD on Break the Targets with every character",
            "BTP_6": "Complete 6 different Break the Targets stages",
            "BTT_6": "Complete 6 different Board the Platforms stages"
        },
        "1p_mode": {
            "BEAT_VE": "Beat Very Easy (5 Stock)",
            "BEAT_N": "Beat Normal (3 Stock)",
            "BEAT_VH": "Beat Very Hard (1 Stock)",
            "BEAT_VH_NC": "Beat Very Hard (1 Stock) w/ No Continues"
        },
        "rng": {},
        "challenge": {
            "ZEBES_SPIKE": "Spike an opponent through the acid on Planet Zebes",
            "SHIELD_BREAK": "Break an opponent's shield",
            "1V3": "Win a 1 v 3 against Level 9 CPUs",
            "STAGE_PKMN_KO": "KO a Stage Pokemon on Saffron City",
            "REFLECTOR_BREAK": "Break Fox's Reflector",
            "200%": "Get an Opponent to 200%",
            "ALLY_KO": "KO an Ally in (1P Game)",
            "4_YOSHIS": "Get 4 Yoshis of the same color on screen"
        }
    },
    "impossible": [
        ["MEME_KO", CLASSIC_LEVELS[10], MEME_MOVES[0]],
        ["MEME_KO", CLASSIC_LEVELS[10], MEME_MOVES[3]]
    ]
};