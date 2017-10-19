"""
Searches module defines all different search algorithms
"""

from graph import graph as g
from graph import utils as u
import heapq

try:
    from queue import *
except ImportError:
    from multiprocessing import Queue
    
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
        
        # Sort current's neighbor using attribute 'data', so that we always choose the left node
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
    frontier = PriorityQueue()
    key = 1
    frontier.put((0,key,initial_node))
    came_from = {}
    cost_so_far = {}
    visited = []
    came_from[initial_node] = None
    cost_so_far[initial_node] = 0
    
    while not frontier.empty():
        current = frontier.get()[2]
        visited.append(current)
        if current == dest_node:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.distance(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(dest_node, next)
                key +=1
                frontier.put((priority,key,next))
                came_from[next] = current

    return getPathEdges(graph,came_from,initial_node,dest_node)


def heuristic(a, b):
    (x1, y1) = a.data.x, a.data.y
    (x2, y2) = b.data.x, b.data.y
    return abs(x1 - x2) + abs(y1 - y2)

def getPathEdges(graph,came_from,initial_node,dest_node):
    
    # Create path
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

