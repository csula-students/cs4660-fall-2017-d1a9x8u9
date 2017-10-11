"""
Searches module defines all different search algorithms
"""
from queue import *
from graph import graph as g
from graph import utils as utl

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    frontier = Queue()    
    frontier.put(initial_node)
    came_from = {}
    came_from[initial_node] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    
    #  CONVERT NODES TO PATH
    current = dest_node 
    path = [current]
    while current != initial_node: 
        current = came_from[current]
        path.append(current)
    path.reverse() 
    
    # Create edges from list 'path'
    edges = []
    for i in range(len(path)-1):
        distance = graph.distance(path[i],path[i+1])
        edge = g.Edge(path[i],path[i+1],distance)
        edges.append(edge) 

    return edges

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
    # frontier = PriorityQueue()
    # frontier.put(initial_node, 0)
    # came_from = {}
    # cost_so_far = {}
    # came_from[initial_node] = None
    # cost_so_far[initial_node] = 0

    # while not frontier.empty():
    #     current = frontier.get()

    #     if current == dest_node:
    #         break
        
    #     for next in graph.neighbors(current):
    #         new_cost = cost_so_far[current] + graph.cost(current, next)
    #         if next not in cost_so_far or new_cost < cost_so_far[next]:
    #             cost_so_far[next] = new_cost
    #             priority = new_cost + heuristic(dest_node, next)
    #             frontier.put(next, priority)
    #             came_from[next] = current
    
    # current = dest_node
    # path = [current]
    # while current != initial_node:
    #     current = came_from[current]
    #     path.append(current)
    # path.append(start)
    # path.reverse()
    
    # edges = []
    # for i in range(len(path) -2):
    #     edges.append(Edge(path[i],path[i+1],1)) 
        
    # return convert_edge_to_grid_actions(path)

    # TODO Get path, convert, and return 

