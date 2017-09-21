"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):

    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """

    # Open file, w = first line and array = the rest of the file
    with open(file_path) as f:
        w = [int(x) for x in next(f).split()]
        array = [[int(x) for x in line.split(':')] for line in f]

    # Convert w into Integer
    intW = int(w[0])
        
    # Construct graph nodes 
    for i in range(intW):
        node = Node(i)
        graph.add_node(node)

    # Iterate through array and get edge information then add graph edge   
    edges = []
    x = 0
    for z in range(len(array)):
        fromNode = Node(array[x][0])
        toNode = Node(array[x][1])
        weight = array[x][2]
        edge = Edge(fromNode,toNode,weight)
        edges.append(edge)
        x = x + 1 
    
    for i in range(len(edges)):
        graph.add_edge(edges[i])

    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        # Check if node_1 is in list, if it is cont. otherwise create node_1 key with node_2 value.
        if node_1 in self.adjacency_list:
            # If node_2 is inside node_1 key, then print out stating so otherwise append node_2 into key.
            if node_2 in self.adjacency_list[node_1]:
                return True
            else:
                return False
        else:
            return False

    def neighbors(self, node):
        # Check to see if node exist, if yes then cont. otherwise print out saying so
        if node in self.adjacency_list:
            # Iterate through the node and print out key + value
            neighbors = []
            for key in self.adjacency_list[node]:
                neighbors.append(key)
            return neighbors
        else:
            return 0

    def add_node(self, node):
        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node] = {}
            return True

    def remove_node(self, node):
        # Couldn't use del in 2d dictionary because it kept breaking out after finding a single match and therefore didn't complete the entire iteration. 
        # So we're using a very bad algorithm to do this.

        # If node exist in list, then delete that node.
        if node in self.adjacency_list:
            del self.adjacency_list[node]

            # Arrays to keep track of key and subkeys 
            x = []
            y = []

            # Iterate through key and subkeys and keep track of index
            for key in self.adjacency_list:
                for k in self.adjacency_list[key]:
                    if k == node:
                        x.append(key)
                        y.append(k)

            # Starting with index 0, use x[r] and y[r] as indexes to remove from adjacency_list
            r = 0
            for i in range(len(x)):
                del self.adjacency_list[x[r]][y[r]]
                r = r + 1

            # Finally return true
            return True

        else:
            return False

    def add_edge(self, edge):
        # Get variables from Object edge
        fromnode = edge.from_node
        tonode = edge.to_node
        weight = edge.weight

        # Check 2d array for fromnode and tonode, if NOT found add otherwise print out error
        if fromnode in self.adjacency_list:
            if tonode in self.adjacency_list[fromnode]:
                return False
            else: 
                self.adjacency_list[fromnode][tonode] = weight
                return True
        else:
                return False

    def remove_edge(self, edge):
        # Get variables from Object edge
        fromnode = edge.from_node
        tonode = edge.to_node

        # Check 2d array for fromnode and tonode, if found delete otherwise print out error
        if fromnode in self.adjacency_list:
            if tonode in self.adjacency_list[fromnode]:
                del self.adjacency_list[fromnode][tonode]
                return True
            else:
                return False
        else:
            return False

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    def __get_node_index(self, node):
        """helper method to find node index"""
        pass

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

