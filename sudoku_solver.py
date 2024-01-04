from sudoku import Sudoku

puzzle = Sudoku(2).difficulty(0.5)
puzzle.show()
board = puzzle.board
print(board)
set_list = {}
constraint_graph = {}

def construct_domain(variable, key):
    """
    Construct a domain for the given variable.
    """
    set_list[key] = set(range(1, len(board) + 1))
    #print(set_list)

def construct_set_list(board):
    """
    Construct a constraint graph for the given board.
    """
    for i in range(len(board)):
        #print(board[i])  # prints first row
        for j in range(len(board[i])):
            #print(board[i][j])  # prints the element in cell i,j
            if board[i][j] is None:
                construct_domain(board[i][j], (i, j))
            else:
                set_list[(i, j)] = {board[i][j]}

def construct_constraint_graph(board):
    """
    Construct a constraint graph for the given board.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            constraint_graph[(i, j)] = set()
            for k in range(len(board)):
                if k == i or k == j:
                    continue
                constraint_graph[(i, j)].add((i, k))
                constraint_graph[(i, j)].add((k, j))




construct_set_list(board)
print(set_list)
construct_constraint_graph(board)
print(constraint_graph)
