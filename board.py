from random import choice


class BingoBoard:
    SIZE = 5, 5
    VALUE = [
        3, 2, 2, 2, 3,
        2, 3, 2, 3, 2,
        2, 2, 4, 2, 2,
        2, 3, 2, 3, 2,
        3, 2, 2, 2, 3
    ]
    SQUARES = [
        "aa", "ab", "ac", "ad", "ae",
        "ba", "bb", "bc", "bd", "be",
        "ca", "cb", "cc", "cd", "ce",
        "da", "db", "dc", "dd", "de",
        "ea", "eb", "ec", "ed", "ee"
    ]
    ROWS = [
        SQUARES[0: 5],
        SQUARES[5: 10],
        SQUARES[10: 15],
        SQUARES[15: 20],
        SQUARES[20:]
    ]
    COLS = [
        [s[0] for s in ROWS],
        [s[1] for s in ROWS],
        [s[2] for s in ROWS],
        [s[3] for s in ROWS],
        [s[4] for s in ROWS]
    ]
    D1 = [
        ROWS[0][0],
        ROWS[1][1],
        ROWS[2][2],
        ROWS[3][3],
        ROWS[4][4]
    ]
    D2 = [
        ROWS[4][0],
        ROWS[3][1],
        ROWS[2][2],
        ROWS[1][3],
        ROWS[0][4]
    ]
    BINGOS = ROWS + COLS + [D1, D2]

    def __init__(self):
        self.goals = {}

    def get_value(self, square):
        row, col = self.get_square_index(square)
        r, c = self.SIZE
        i = (r * row) + col

        return self.VALUE[i]

    def get_square_hash(self, row, col):
        r, c = self.SIZE
        i = (r * row) + col

        return self.SQUARES[i]

    def get_square_index(self, square):
        i = self.SQUARES.index(square)

        return i // 5, i % 5

    def get_bingos(self, row, col):
        output = []
        square = self.get_square_hash(row, col)

        for b in self.BINGOS:
            if square in b:
                output.append(b)

        return output

    def get_k_squares(self):
        squares = self.SQUARES.copy()
        output = []

        for i in range(5):
            try:
                square = choice(squares)
            except IndexError:
                return output

            output.append(square)

            for b in self.get_bingos(*self.get_square_index(square)):
                for s in b:
                    if s in squares:
                        squares.remove(s)

        return output

    @staticmethod
    def compare_k_sets(k1, k2):
        return any([e in k1 for e in k2])

    def get_k_sets(self):
        uniques = []

        for i in range(500):
            k = (self.get_k_squares())

            if len(uniques) == 0:
                uniques.append(k)
            else:
                new = True
                for k_set in uniques:
                    if self.compare_k_sets(k_set, k):
                        new = False

                if new:
                    uniques.append(k)

        return uniques

    def get_k_set_value(self, k_set):
        return sum([
            self.get_value(s) for s in k_set
        ])

    def add_goal(self, square, goal):
        self.goals[square] = goal

    def add_rand_goals(self, squares, normal, hard=None):
        for s in squares:
            choices = normal
            if self.get_value(s) > 2:
                if hard:
                    choices = hard

            goal = choice(choices)
            if len(choices) > 1:
                choices.remove(goal)

            self.add_goal(s, goal)

    def squares_left(self):
        return [
            s for s in self.SQUARES if s not in self.goals
        ]
