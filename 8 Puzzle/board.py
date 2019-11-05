class BoardState:

    PERFECT_BOARD_INDICES = {
                                [[1, 2, 3], [4, 5, 6], [7, 8, 0]][x][y] :
                                    {
                                        'row': x,
                                        'col': y
                                    }
                                for x in range(3)
                                for y in range(3)
                            }

    def __init__(self, board, parent):
        self.parent = parent
        self.board = board
        self.stepcost = self.findsteps()
        self.manhattan = self.manhattan_distance()
        self.priority = self.manhattan + self.stepcost


    def findsteps(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.stepcost + 1

    def md_calc(self, value, x, y):

        perfect_row = self.PERFECT_BOARD_INDICES[value]['row']
        perfect_col = self.PERFECT_BOARD_INDICES[value]['col']


        return abs(x - perfect_row) + abs(y - perfect_col)

    def manhattan_distance(self):

        manhattans = [self.md_calc(self.board[x][y], x, y) for x in range(3) for y in range(3)]


        return sum(manhattans)
