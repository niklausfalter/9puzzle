class BoardState:
"""This class defines a Board State object; each iteration/configuration of the board is initiated as its own object with its own properties."""

    PERFECT_BOARD_INDICES = {
                                [[1, 2, 3], [4, 5, 6], [7, 8, 0]][x][y] :
                                    {
                                        'row': x,
                                        'col': y
                                    }
                                for x in range(3)
                                for y in range(3)
                            }

    # Each instance keeps track of its parent, as well as other important properties.
    # These are found by running functions when the object is instantiated to populate these properties
    def __init__(self, board, parent):
        self.parent = parent
        self.board = board
        self.stepcost = self.findsteps()
        self.manhattan = self.manhattan_distance()
        self.priority = self.manhattan + self.stepcost

    # This function finds the steps
    def findsteps(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.stepcost + 1
    
    # This function calcs the mds
    def md_calc(self, value, x, y):

        perfect_row = self.PERFECT_BOARD_INDICES[value]['row']
        perfect_col = self.PERFECT_BOARD_INDICES[value]['col']

        return abs(x - perfect_row) + abs(y - perfect_col)

    # This function distances the manhattans
    def manhattan_distance(self):

        manhattans = [self.md_calc(self.board[x][y], x, y) for x in range(3) for y in range(3)]
        return sum(manhattans)
