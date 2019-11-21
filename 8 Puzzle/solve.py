from board import BoardState
from queue import Queue
import copy


def swap(board,x,y,x1,y1):

    board1 = copy.deepcopy(board.board)
    board1[x][y], board1[x1][y1] = board1[x1][y1], board1[x][y]
    return BoardState(board1, board)


def create_children(brd):

    board = brd.board
    children = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                
                if not x:
                    children.append(swap(brd, x, y, x+1, y))
                elif x == 1:
                    children.append(swap(brd, x, y, x - 1, y))
                    children.append(swap(brd, x, y, x + 1, y))
                else:
                    children.append(swap(brd, x, y, x - 1, y))
                    
                if not y:
                    children.append(swap(brd, x, y, x, y + 1))
                elif y == 1:
                    children.append(swap(brd, x, y, x, y + 1))
                    children.append(swap(brd, x, y, x, y - 1))
                else:
                    children.append(swap(brd, x, y, x, y - 1))
                break
    
    # My children are broken, please I would like to
    return children


def is_possible(board):

    inversions = 0
    a = [board[x][y] for x in range(3) for y in range(3)]
    b = [board[x][y] for x in range(3) for y in range(3)]


    b.sort()
    for x in range(9):
        if b[x] != x:
            print('Invalid value found in board')
            return False

    a.remove(0)
    for x in a:
        f = a.index(x)
        g = a[f:]
        for y in g:
            if y > x:
                inversions += 1
    
    print('Number of Inversions:', inversions)
    if inversions % 2 == 0:
        return True
    else:
        return False


def solve_board(board):

    #this prints out the board or says not cool if it is not possible
    show_board(board)
    if not is_possible(board):
        print("Bro, not cool. Enter a valid board next time.")
        return
    q = Queue()
    q.put(BoardState(board, None))

    goal_state = [
       [1,2,3],
        [4,5,6],
        [7,8,0],
        ]

    visited = Queue()
    while True:
        current = q.push()
        visited.put(current)
        if current.board == goal_state:
            print('Board solved successfully!!')
            show_board(current.board)            
            return
        a = create_children(current)
        for x in a:
            if q.instances(x) == 0 and visited.instances(x) == 0:
                q.put(x)
            elif q.instances(x) != 0:
                q[0].stepcost = 0


def show_board(board):
        print('\n')
        print('\n  -----------')

        for row in board:
            print(' |', end=' ')
            for column in row:
                print(str(column), end=' | ')
            print('\n  -----------')
        print('\n')
        return ''
