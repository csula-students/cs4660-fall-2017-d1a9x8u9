"""
Searches module defines all different search algorithms
"""
from queue import *
from graph import graph as g
import heapq

def bfs(graph, initial_node, dest_node):
    # BFS FIFO
    frontier = Queue()    
    frontier.put(initial_node)
    came_from = {}
    came_from[initial_node] = None

    while not frontier.empty():

        current = frontier.get()

        if current == dest_node:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current 

    return getPathEdges(graph,came_from,initial_node,dest_node)

def dfs(graph, initial_node, dest_node):

    # DFS is LIFO
    frontier = [initial_node]
    came_from = {}
    came_from[initial_node] = None

    while frontier:

        current = frontier.pop()

        if current == dest_node:
            break
        
        n = graph.neighbors(current)
        
        # Sort current's neighbor using attribute 'data'. 
        # I had to do this because some of the neighbor list's were in reversed order compared to what the test cases expected.
        n.sort(key=lambda x: x.data, reverse=True)

        for next in n:
            frontier.append(next)
            came_from[next] = current

    return getPathEdges(graph,came_from,initial_node,dest_node)

def dijkstra_search(graph, initial_node, dest_node):

    # Need key in order to compare Node()'s
    key = 1 
    frontier = PriorityQueue()
    frontier.put((0,key,initial_node))

    came_from = {}
    distance_so_far = {}
    came_from[initial_node] = None
    distance_so_far[initial_node] = 0

    while not frontier.empty():

        current = frontier.get()[2]
        if current == dest_node:
            break
        
        for next in graph.neighbors(current):
            new_distance = distance_so_far[current] + graph.distance(current, next)
            if next not in distance_so_far or new_distance < distance_so_far[next]:
                distance_so_far[next] = new_distance
                priority = new_distance
                came_from[next] = current
                key +=1
                frontier.put((priority,key,next))
    
    return getPathEdges(graph,came_from,initial_node,dest_node)

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

def getPathEdges(graph,came_from,initial_node,dest_node):
    
    current = dest_node 
    path = [current]
    while current != initial_node: 
        current = came_from[current]
        path.append(current)
    path.reverse() 
    
    print(path)
    # Create edges from list 'path'
    edges = []
    for i in range(len(path)-1):
        distance = graph.distance(path[i],path[i+1])
        edge = g.Edge(path[i],path[i+1],distance)
        edges.append(edge) 

    return edges

