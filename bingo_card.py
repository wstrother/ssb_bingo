import json
import random
import constants as goal

K, N = "keys", "number"

DISTRIBUTION = [
    # 6 single choice categories
    {K: [goal.BEAT_VE_CHOICE], N: 1},
    {K: [goal.BEAT_N_CHOICE], N: 1},
    {K: [goal.BEAT_VH_CHOICE], N: 1},
    {K: [goal.BTT_CHOICE], N: 1},
    {K: [goal.BTP_CHOICE], N: 1},
    {K: [goal.MEME_KO], N: 1},

    # 5 modified bonus game goals
    {K: [
        goal.BTT_B_MOVE,
        goal.BTP_FAST,
        goal.BTT_FAST
    ], N: 5},

    # 5 item/stage goals
    {K: [
        goal.HEAL_3,
        goal.WPN_KO,
        goal.STAGE_KO
    ], N: 4},
    {K: [goal.PKMN_CATCH], N: 1},

    # 5 1P mode bonus goals
    {K: [goal.BONUS], N: 5},

    # 4 random unique goals
    {K: [goal.UNIQUE_KEY], N: 4}
]


def get_goals(amount, goal_dict, *keys):
    goals = []
    for key in keys:
        goals += goal_dict[key]

    return random.sample(goals, amount)


if __name__ == "__main__":
    file = open("goal_dict.json", "r")
    gd = json.load(file)
    file.close()

    bingo_card = []
    for item in DISTRIBUTION:
        bingo_card += get_goals(
            item[N], gd, *item[K]
        )

    random.shuffle(bingo_card)
    for b in bingo_card:
        print(b)

    bingo_card = [{"name": g} for g in bingo_card]
    file = open("bingo_card.json", "w")
    json.dump(bingo_card, file, indent=2)
    file.close()
