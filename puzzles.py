
import numpy as np

class Node:
    
    def __init__(self, state, parents, child, gscore, hscore, fscore):
        self.state = state        # The current state (board itself)
        self.parents = parents    # Whether it has parents or not
        self.child = child        # Whether it has child or not
        self.gscore = gscore      # Depth (path cost)
        self.hscore = hscore      # Heuristic cost
        self.fscore = fscore      # fscore = gscore + hscore
        self.parents_node = None # parents node for tracking the path
        self.max_nodes = 0  
        self.key = 0
        
    def __lt__(self, other):
        # Compare the node class itself 
        return self.fscore
    
class Puzzle:
    
    def __init__(self, initial, goal):
        self.initial_state = initial # Initial state
        self.goal = goal             # Goal state
        self.parents = 0             # Whether it has parents or not
        self.child = 0               # Whether it has child or not
        self.gscore = 0              # Depth (path cost)
        self.hscore = 0              # Heuristic cost
        self.fscore = 0              # fscore = gscore + hscore
        self.key_sets = set()        # sets including unique keys of duplicated states
        self.expanded_nodes = 0      # The number of expanded nodes
        
    def goal_test(self, state):
        self.state = state
        self.diff = abs(self.goal - state).sum()
        
        self.expanded_nodes +=1
        # Add the current node's key
        self.key_sets.add(make_key(state))
        # Find the possible movements from the current states
        self.operators = self.update_operator()
        
        if self.diff == 0:
            # Goal state
            return True 
        else:
            return False
        
    def update_operator(self):
        # Get the index of empty tile (0)
        self.zero_idx = np.where(self.state == 0)
        x = self.zero_idx[0][0]
        y = self.zero_idx[1][0]
        valid_operations = []
        for op in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x1 = x + op[0]
            y1 = y + op[1]
            if (x1>=0) and (x1<=2) and(y1>=0) and (y1<=2):
                # Check possible moves inside the tile
                valid_operations.append([x, y, x1, y1])
        return valid_operations
    
def make_key(board):
    # Make a unique for the given board e.g., '12345678'
    lst = board.flatten().tolist()
    lst = [str(i) for i in lst]
    key = ''.join(lst)
    return key 