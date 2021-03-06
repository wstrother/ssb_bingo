import json
from goals import TEMPLATES, UNIQUE, UNIQUE_KEY, IMPOSSIBLE

"""
This file is used to generate the "goal_list.json" dictionary.
If you are downloading this repository to generate your own bingo cards,
this will already be done for you, so you probably don't need to worry
about running this script, unless you know how to edit the constants
file in order to generate your own set of goals.
"""


# These methods define how to fill out the different templates with
# all the unique permutations that can be generated by each set of
# template choices. I tried really hard to figure out how to write
# these all in one big recursive function but for some reason it was
# breaking my brain, so I did it this way.

def fill_depth_1(template, fill):
    output = []

    for item in fill:
        new_goal = template.format(item)
        if new_goal not in IMPOSSIBLE:
            output.append(new_goal)

    return output


def fill_depth_2(template, fill_a, fill_b):
    output = []
    selections = []

    for a in fill_a:
        selections.append(a)

        for b in [x for x in fill_b if x not in selections]:
            new_goal = template.format(a, b)
            if new_goal not in IMPOSSIBLE:
                output.append(new_goal)

    return output


def fill_depth_3(template, fill_a, fill_b, fill_c):
    output = []
    selections_a = []

    for a in fill_a:
        selections_a.append(a)
        selections_b = []

        for b in [x for x in fill_b if x not in selections_a]:
            selections_b.append(b)

            for c in [x for x in fill_c if x not in selections_b + selections_a]:
                new_goal = template.format(a, b, c)
                if new_goal not in IMPOSSIBLE:
                    output.append(new_goal)

    return output


if __name__ == "__main__":

    # add the unique goals

    goals = {UNIQUE_KEY: UNIQUE}

    for key in TEMPLATES:
        choices = TEMPLATES[key]
        goal_list = []

        # add all the permutations based on the templates dictionary

        if len(choices) == 1:
            goals[key] = fill_depth_1(key, *choices)

        if len(choices) == 2:
            goals[key] = fill_depth_2(key, *choices)

        if len(choices) == 3:
            goals[key] = fill_depth_3(key, *choices)

    # output 'goals' dict as a JSON file

    file = open("goal_dict.json", "w")
    json.dump(goals, file, indent=2)
    file.close()
