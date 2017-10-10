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
    with open(file_path) as f:
        content = f.readlines()

    # Create a List for each line in 'content'
    content= [x.strip() for x in content]
    
    # 'mode_content' will hold the modified content list
    filteredContent = []

    # If the row starts with '+' or '-' then ignore. else add the row to filteredContent 
    for row in content:
        if row[0] == '+' or row[0] == '-':
            continue
        else: 
            # Take the '|' out from the row and append to 'filteredContent'
            filteredContent.append(row[1:len(row)-1])
    
    # Go through rows. For each row and using step_size=2, check if node. If yes then add to graph, else ignore.
    y = 0
    for row in filteredContent:
        for x in range(0,len(row),2):
            if row[x] == '#':
                continue
            else:
                node = g.Node(Tile(x,y,filteredContent[y][x]))
                graph.add_node(node)
                # Add neighbors

                # Check top Tile
                if y > 0:
                    if(filteredContent[y-1][x] == '#'):
                        continue
                    else:
                        # Create node 
                        NodeToCheck = g.Node(Tile(x,y-1,filteredContent[y-1][x]))
                        
                        # Check if current index node is adjacent to top node
                        if(graph.adjacent(node,NodeToCheck)):
                            print('Edge already here')
                        else:
                            edge = g.Edge(node,NodeToCheck,1)
                            graph.add_edge(edge)

                # Check bottom Tile
                if y < len(filteredContent) - 1:
                    if(filteredContent[y+1][x] == '#'):
                        continue
                    else:
                        # Create node 
                        NodeToCheck = g.Node(Tile(x,y+1,filteredContent[y+1][x]))
                        # Check if current index node is adjacent to top node
                        if(graph.adjacent(node,NodeToCheck)):
                            print('Edge already here')
                        else:
                            edge = g.Edge(node,NodeToCheck,1)
                            graph.add_edge(edge)

                # Check right Tile
                if x < len(row) - 2:
                    if(filteredContent[y][x+2] == '#'):
                        continue
                    else:
                        # Create node 
                        NodeToCheck = g.Node(Tile(x+2,y,filteredContent[y][x+2]))
                        
                        # Check if current index node is adjacent to top node
                        if(graph.adjacent(node,NodeToCheck)):
                            print('Edge already here')
                        else:
                            edge = g.Edge(node,NodeToCheck,1)
                            graph.add_edge(edge)
             
                # Check left Tile
                if x > 1:
                    if(filteredContent[y][x-2] == '#'):
                        continue
                    else:
                        # Create node 
                        NodeToCheck = g.Node(Tile(x-2,y,filteredContent[y][x-2]))
                        
                        # Check if current index node is adjacent to top node
                        if(graph.adjacent(node,NodeToCheck)):
                            print('Edge already here')
                        else:
                            edge = g.Edge(node,NodeToCheck,1)
                            graph.add_edge(edge)   
        y = y + 1
    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    action = []
    for edge in edges:

        tile1 = edge.from_node
        tile2 = edge.to_node
        weight = edge.weight    
    
        tile1x = tile1.x
        tile1y = tile1.y   

        tile2x = tile2.x
        tile2y = tile2.y

        x = tile2x - tile1x
        y = tile2y - tile1y

        if x == 0:
            if y > 0:
                action.append("S")
            else:
                action.append("N")
        else:
            if x > 0:
                action.append("E")
            else:
                action.append("W")

    print(action)
    return action
