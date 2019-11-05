from solve import solve_board
from random import randint


def generate_board():

    num_list = [x for x in range(9)]

    puzzle = [[num_list.pop(randint(0, len(num_list) - 1)) for x in range(3)] for y in range(3)]
    return puzzle


solve_board(generate_board())
