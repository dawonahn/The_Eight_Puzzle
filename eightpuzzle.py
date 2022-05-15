
import time
from puzzles import *
from solvers import *
from utils import *


def print_path(node):
    
    paths = []

    while True:
        paths.append(node.state)
        node = node.parents_node
        if node is None:
            break
        
    print('---------------------------------------------------------')
    print('------------------------path-----------------------------')
    for p in paths[::-1]:
        board = p.tolist()
        for j in range(len(board)):
            print(board[j])
            
        print('---------------------------------------------------------')
def start_puzzle_game(number=None, random_board=None, solver=None):
    
        if random_board is None:
            if number == 1:
                board = np.array([[1, 2, 3], 
                      [4, 5, 6], 
                     [7, 8, 0]])
            if number == 2:
                board = np.array([[1, 2, 3], 
                          [4, 5, 6], 
                         [0, 7, 8]])
            if number == 3:
                board = np.array([[1, 2, 3], 
                          [5, 0, 6], 
                         [4, 7, 8]])
            if number == 4:
                board = np.array([[1, 3, 6], 
                          [5, 0, 2], 
                         [4, 7, 8]])
            if number == 5:
                board = np.array([[1, 3, 6], 
                          [5, 0, 7], 
                         [4, 8, 2]])
            if number == 6:
                board = np.array([[1, 6, 7], 
                          [5, 0, 3], 
                         [4, 8, 2]])
            if number == 7:
                board = np.array([[7, 1, 2], 
                          [4, 8, 5], 
                         [6, 3, 0]])
            if number == 8:
                board = np.array([[0, 7, 2], 
                          [4, 6, 1], 
                         [3, 5, 8]])
        else:
            board = random_board
        
        goal = np.array([[1, 2, 3], 
                          [4, 5, 6], 
                         [7, 8, 0]])

        if solver == 1:
            queuing_function = UniformCost
        if solver == 2:
            queuing_function = AStar_Misplaced
        if solver == 3:
            queuing_function = AStar_Manhattan
        # Find the solution
        
        print("-------------------- Starting Solving --------------------")
        problem = Puzzle(board, goal)
        final_node = general_search(problem, queuing_function)
        print_path(final_node)
        
if __name__ == '__main__':
    
    print("-------------------- The 8-Puzzle --------------------")

    option = int(input('Type 1. Examples or 2. Type random state: '))
    
        
    if option == 1:
        number = int(input('\nType number form 1-9 (The higher, the more difficult): '))
        initial_state = None
    else:
        number = 0
        print('Type initial state: ')
        row1 = input('first row (e.g., 1 2 3): ')
        row2 = input('second row (e.g., 4 5 6): ')
        row3 = input('third row (e.g., 7 8 0): ')
        
        lst = []
        row1 = row1.split(' ')
        row1 = [int(i) for i in row1]
        row2 = row2.split(' ')
        row2 = [int(i) for i in row2]
        row3 = row3.split(' ')
        row3 = [int(i) for i in row3]
        initial_sate = np.array([row1, row2, row3])
        
    solver = int(input("\nType\n1. Uniform Cost\n2. A* with Misplaced Tile\n3. A* with Manhattan Distance: "))
    
    start_puzzle_game(number, initial_state, solver)
                
        
            