import json
from random import choice
import goals
from board import BingoBoard

file = open("goal_dict.json")
GOAL_DICT = json.load(file)
file.close()

BONUS_GAME_GOALS = [
    goals.BONUS_BOTH,
    goals.BTT_CHOICE,
    goals.BTP_CHOICE,
    goals.BTT_B_MOVE,
] + goals.UNIQUE_BONUS

SPEEDRUN_GOALS = [
    goals.BEAT_VE_CHOICE,
    goals.BEAT_N_CHOICE,
    goals.BEAT_VH_CHOICE,
] + goals.UNIQUE_SPEEDRUN

RNG_GOALS = [
    goals.WPN_KO,
    goals.HEAL_3,
    goals.PKMN_CATCH,
    goals.STAGE_KO
] + goals.UNIQUE_RNG

POINTS_GOALS = [
    goals.POINTS
]

CHALLENGE_GOALS = [
    goals.MEME_KO
] + goals.UNIQUE_CHALLENGE

HARD_GOALS = [
    goals.BTT_B_MOVE,
    goals.BEAT_VH_CHOICE,
    goals.STAGE_KO,
    goals.HEAL_3,
    goals.MEME_KO,
    goals.UNIQUE_BONUS[-1],
    goals.UNIQUE_BONUS[-2],
    goals.UNIQUE_SPEEDRUN[-1],
    goals.UNIQUE_RNG[0]
]


def add_from_goals(board, squares, goal_set):
    normal = [g for g in goal_set if g not in HARD_GOALS]
    hard = [g for g in goal_set if g not in normal]

    board.add_rand_goals(squares, normal, hard)


def get_from_template(template):
    g = choice(GOAL_DICT[template])
    GOAL_DICT[template].remove(g)

    return g


if __name__ == "__main__":
    bb = BingoBoard()
    k_sets = bb.get_k_sets()
    k_sets.sort(key=lambda k: bb.get_k_set_value(k))

    used = sum([len(k) for k in k_sets])
    print("{} squares used:".format(used))
    for k in k_sets:
        print(k)

    # add bonus game goals to least valuable k set
    add_from_goals(bb, k_sets.pop(0), BONUS_GAME_GOALS)

    # add speedrun goals to most valuable k set
    add_from_goals(bb, k_sets.pop(-1), SPEEDRUN_GOALS)

    if len(k_sets) == 1:
        add_from_goals(bb, k_sets[0], RNG_GOALS)
        add_from_goals(
            bb,
            bb.squares_left(),
            CHALLENGE_GOALS + POINTS_GOALS
        )

    elif len(k_sets) == 2:
        add_from_goals(bb, k_sets[0], RNG_GOALS)
        add_from_goals(bb, k_sets[1], CHALLENGE_GOALS)
        add_from_goals(bb, bb.squares_left(), POINTS_GOALS)

    elif len(k_sets) == 3:
        add_from_goals(bb, k_sets[0], RNG_GOALS)
        add_from_goals(bb, k_sets[1], CHALLENGE_GOALS)
        add_from_goals(bb, k_sets[2], POINTS_GOALS)

    if bb.squares_left():
        add_from_goals(bb, bb.squares_left(), POINTS_GOALS)

    json_goals = []
    for square in bb.SQUARES:
        goal_name = bb.goals[square]
        if "{}" in goal_name:
            goal_name = get_from_template(goal_name)

        print(square, goal_name)

        json_goals.append({
            "name": goal_name
        })

    file = open("bingo_card.json", "w")
    json.dump(json_goals, file, indent=4)
    file.close()
