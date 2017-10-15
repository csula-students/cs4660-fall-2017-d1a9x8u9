"""
utils package is for some quick utility methods

such as parsing
"""

from . import graph as g

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    # Open file and read
    f = open(file_path)

    rows = []

    for line in f:
        if line[0] == '+' or line[0] == '-':
            continue
        filteredrow = line[1:-2]
        rows.append([filteredrow[i:i+2] for i in range(0, len(filteredrow), 2)])
    
    f.close()

    nodes = []
    edges = []

    y = 0
    for row in rows:
        x = 0
        for block in row:
            if block == '##':
                x += 1
                continue

            curr_node = g.Node(Tile(x, y, block))
            nodes.append(curr_node)
            
            right = (x + 1, y)
            left = (x - 1, y)
            up = (x, y + 1)
            down = (x, y - 1)
            neighbors = [right,left,up,down]   
            
            for neighbor in neighbors:
                if neighbor[0] >= len(rows[0]) or neighbor[0] < 0 or neighbor[1] >= len(rows) or neighbor[1] < 0:   # Bound check
                    continue
                neighbor_block = rows[neighbor[1]][neighbor[0]]
                if neighbor_block == '##':
                    continue
                
                neighbor_node = g.Node(Tile(neighbor[0], neighbor[1], neighbor_block))
                edges.append(g.Edge(curr_node, neighbor_node, 1))
            
            x += 1
        y += 1

    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(edge)

    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    actions = []

    for edge in edges:
        
        if edge.from_node.data.x > edge.to_node.data.x:
            actions.append('W')
        elif edge.from_node.data.x < edge.to_node.data.x:
            actions.append('E')
        elif edge.from_node.data.y > edge.to_node.data.y:
            actions.append('N')
        else:
            actions.append('S')

    return ''.join(actions)
