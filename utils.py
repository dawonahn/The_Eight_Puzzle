
import heapq
import numpy as np
from puzzles import *

def make_node(initial_state):            
    # Make the node with the initial state
    return Node(initial_state, 0, 0, 0, 0, 0)


def make_queue(node):
    # Put the node into queue
    nodes = []
    heapq.heappush(nodes, (node.fscore, node))
    return nodes


def empty(nodes):
    # Check the if the queue is empty
    if len(nodes) == 0:
        print("Failure")
        return True
    else:
        return False
    
    
def remove_front(nodes):
    # Pop the first node of the queue
    return heapq.heappop(nodes)


def update_move(op, node):
    # Update the move with the given possible move
    x, y, x1, y1 = op
    new_state = node.state.copy()
    new_state[x1, y1] = node.state[x, y]
    new_state[x, y] = node.state[x1, y1]
    return new_state


def expand(node, operators, problem):
    # Exapand the child nodes
    # node: current node
    # operators: possible moves
    # problems: used fo key sets

    child = []
    for op in operators:
        new_state = update_move(op, node)
        key = make_key(new_state)         
        if key not in problem.key_sets:
            node.child = 1
            cnode = Node(new_state, 1, 0, node.gscore + 1, 0, 0)
            cnode.key = key
            cnode.parents_node = node
            child.append(cnode)
    return child


def UniformCost(nodes, child_nodes, goal=None):
    # Get the node with the minimium path cost
    for cnode in child_nodes:
        heapq.heappush(nodes, ((cnode.gscore), cnode))
    return nodes


def AStar_Misplaced(nodes, child_nodes, goal):
    # Get the node with the minimium cost sum of path cost and the heuristic
    goal = goal.flatten()[:-1]
    
    for cnode in child_nodes:
        b = cnode.state.flatten()[:-1]
        cnode.hscore = np.count_nonzero(abs(b-goal))
        cnode.fscore = cnode.gscore + cnode.hscore   
        heapq.heappush(nodes, ((cnode.fscore), cnode))
    return nodes


def AStar_Manhattan(nodes, child_nodes, goal):
    # Get the node with the minimium cost sum of path cost and the heuristic
    for cnode in child_nodes:
        cnode.hscore = manhattan_distance(cnode.state, goal)
        cnode.fscore = cnode.gscore + cnode.hscore   
        heapq.heappush(nodes, ((cnode.fscore), cnode))
    return nodes


def manhattan_distance(A, goal):
    # Calculate the Mahnhattan distance between two states
    b_idxs = []
    g_idxs = []
    a, b = goal.shape
    for i in range(1, a*b):
        a,b = np.where(A == i)
        c,d = np.where(goal == i)
        b_idxs.append([a[0], b[0]])
        g_idxs.append([c[0], d[0]])
    hscore = (np.abs(np.array(b_idxs) - np.array(g_idxs))).sum()
    return hscore

        