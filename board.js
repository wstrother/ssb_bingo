
class Board {
    SIZE = [5, 5];
    VALUE = [
        3, 2, 2, 2, 3,
        2, 3, 2, 3, 2,
        2, 2, 4, 2, 2,
        2, 3, 2, 3, 2,
        3, 2, 2, 2, 3
    ];
    SQUARES = [
        "aa", "ab", "ac", "ad", "ae",
        "ba", "bb", "bc", "bd", "be",
        "ca", "cb", "cc", "cd", "ce",
        "da", "db", "dc", "dd", "de",
        "ea", "eb", "ec", "ed", "ee"
    ];
    ROWS = [
        this.SQUARES.slice(0, 5),
        this.SQUARES.slice(0, 5),
        this.SQUARES.slice(5, 10),
        this.SQUARES.slice(10, 15),
        this.SQUARES.slice(15, 20),
        this.SQUARES.slice(20)
    ];
    COLS = [
        this.SQUARES.filter(s => s[0]),
        this.SQUARES.filter(s => s[1]),
        this.SQUARES.filter(s => s[2]),
        this.SQUARES.filter(s => s[3]),
        this.SQUARES.filter(s => s[4])
    ];
    D1 = [
        this.ROWS[0][0],
        this.ROWS[1][1],
        this.ROWS[2][2],
        this.ROWS[3][3],
        this.ROWS[4][4]
    ];
    D2 = [
        this.ROWS[4][0],
        this.ROWS[3][1],
        this.ROWS[2][2],
        this.ROWS[1][3],
        this.ROWS[0][4]
    ];
    BINGOS = this.ROWS.concat(this.COLS, this.D1, this.D2);

    constructor() {
        this.goals = {};
    }

    getIndex([row, col]) {
        let width = this.SIZE[0];
        return (row * width) + col;
    }
    
    getGridIndex(square) {
        let i = this.SQUARES.indexOf(square);
        return [Math.floor(i / 5), i % 5];
    }

    getHash([row, col]) {
        return this.SQUARES[this.getIndex([row, col])];
    }
    
    getValue(square) {
        return this.VALUE[this.SQUARES.indexOf(square)];
    }

    getBingos(square) {
        return this.BINGOS.filter(bingo => bingo.includes(square));
    }

    // get an individual K set
    // pick up to 5 squares at random that don't share any bingos
    getKSquares(squares) {
        let output = [];
        let square;

        for (i = 0; i < 5; i++) {
            if (squares) {
                square = squares[Math.floor(Math.random * squares.length)];
            } else {
                return output;
            }
            
            output.push(square);
            
            this.get_bingos(square).forEach(bingo => {
                bingo.forEach(square => {
                    squares.splice(squares.indexOf(square), 1);
                });
            });
        }

        return output;    
    }

    // generate K sets until there are no more squares left
    // then order them by their total value
    getKSets() {
        let squares_left = this.SQUARES.copy();
        let k;
        let k_sets = [];

        while (squares_left) {
            k = this.getKSquares(squares_left);
            k_sets.push(k);
            k.forEach(square => {
                squares_left.splice(squares_left.indexOf(square), 1);
            });
        }

        return k_sets.sort(k => k.reduce((sum, square) => sum + this.getValue(square), 0));
    }

    addGoal(square, goal) {
        this.goals[square] = goal;
    }

    

}