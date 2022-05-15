
from utils import *

def general_search(problem, queuing_function):
    
    nodes = make_queue(make_node(problem.initial_state))
    max_nodes = 0
    while True:
        if empty(nodes):
            break;
        _, node = remove_front(nodes)    
        if problem.goal_test(node.state):
            # frontier nodes
            node.queue_nodes = max(len([n for _, n in nodes if n.child == 0]), max_nodes)
            # expanded nodes
            node.expanded_nodes = problem.expanded_nodes
            print(f"Final|| Solution depth: {node.gscore}\tExpanded : {node.expanded_nodes}\tSpace: {node.queue_nodes}")
            return node
    
        nodes = queuing_function(nodes, expand(node, problem.operators, problem), problem.goal)
        max_nodes = max(len(nodes), max_nodes)