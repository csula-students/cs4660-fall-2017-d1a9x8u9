"""
Searches module defines all different search algorithms
"""
from queue import *
from graph import graph as g

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # Knowing BFS is FIFO, we'll create a Queue 'frontier' and put in our start node 'initial_node'. We also create/initalize a dictionary 'came_from'
    # with 'initial_node' to keep track of direction - keeping in mind that 'inital_node' does not have a direction 
    frontier = Queue()    
    frontier.put(initial_node)
    came_from = {}
    came_from[initial_node] = None

    # Keep looping as long as frontier !empty.
    while not frontier.empty():

        # Get item from frontier and assign to 'current' and will be used as this iteration's main data source
        current = frontier.get()

        # Exit while loop if current = dest_node
        if current == dest_node:
            break
        
        # Get current's neighbors and iterate though 
        for next in graph.neighbors(current):
            # If came_from has never seen this, enque and set 'next''s parent to current
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current 

    # Get path's edge and return
    return getPathEdges(graph,came_from,initial_node,dest_node)

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # Since DFS is LIFO, create a LIST 'frontier' and input start node 'initial_node'. We also create/initalize a dictionary 'came_from'
    # with 'initial_node' to keep track of direction - keeping in mind that 'inital_node' does not have a direction 
    frontier = [initial_node]
    came_from = {}
    came_from[initial_node] = None

    # While frontier !empty
    while frontier:

        # Get item from frontier and assign to 'current' and will be used as this iteration's main data source
        current = frontier.pop()

        # Exit while loop if current = dest_node 
        if current == dest_node:
            break
        
        # Get current's neighbor 
        n = graph.neighbors(current)
        
        # Sort current's neighbor using attribute 'data'. 
        # I had to do this because some of the neighbor list's were in reversed order compared to what the test cases expected.
        n.sort(key=lambda x: x.data, reverse=True)

        # Iterate through neighbors 'n'            
        for next in n:
            # insert 'next' into our stack. Set our 'next''s parent
            frontier.append(next)
            came_from[next] = current

    # Get path's edge and return
    return getPathEdges(graph,came_from,initial_node,dest_node)

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
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
    #     # print('cost_so_far[inital_node]',cost_so_far)
    #     print('current',current)
    #     if current.__eq__(dest_node):
    #         break
        
    #     for next in graph.neighbors(current):
    #         print('next',next)
    #         # print('cost_so_far',cost_so_far)
    #         # print('cost_so_far[current]',cost_so_far[current])
    #         # print('graph.distance(current,next)',graph.distance(current, next))
    #         new_cost = cost_so_far[current] + graph.distance(current, next)
    #         # print('new_cost',new_cost)
    #         if next not in cost_so_far or new_cost < cost_so_far[next]:
    #             cost_so_far[next] = new_cost
    #             # print('cost_so_far[next]',new_cost)
    #             priority = new_cost
    #             # print(priority)
    #             frontier.put(priority,next)
    #             came_from[next] = current

    # #  CONVERT NODES TO PATH
    # current = dest_node 
    # path = [current]
    # print('came_from',came_from)
    # while current != initial_node: 
    #     current = came_from[current]
    #     path.append(current)
    # path.reverse() 
    
    # # Create edges from list 'path'
    # edges = []
    # for i in range(len(path)-1):
    #     distance = graph.distance(path[i],path[i+1])
    #     edge = g.Edge(path[i],path[i+1],distance)
    #     edges.append(edge) 

    # return edges

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
    
    # Create edges from list 'path'
    edges = []
    for i in range(len(path)-1):
        distance = graph.distance(path[i],path[i+1])
        edge = g.Edge(path[i],path[i+1],distance)
        edges.append(edge) 

    return edges

