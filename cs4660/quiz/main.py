"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs
from queue import *


# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def bfs(start,goal):
    frontier = Queue()    
    frontier.put(start)
    came_from = {}
    came_from[start] = None     
    effect_so_far = {}
    effect_so_far[start] = 0

    while not frontier.empty():

        current = frontier.get()
        current_room = get_state(current)

        if current_room['id'] == goal:
            print(effect_so_far[current])
            break

        for i in range(len(current_room['neighbors'])):
            neighbor = current_room['neighbors'][i]['id']

            t_state = transition_state(current_room['id'],neighbor)
            new_effect = effect_so_far[current] + t_state['event']['effect']

            if neighbor not in came_from:
                effect_so_far[neighbor] = new_effect
                came_from[neighbor] = current 
                frontier.put(neighbor)

    current = goal 
    path = [current]
    while current != start: 
        current = came_from[current]
        path.append(current)
    path.reverse()

    print(path)

def dijkstra(start,goal):
    # DIJKSTRA 
    # empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    # print(empty_room)
    # print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))

    frontier = PriorityQueue()
    frontier.put((0,start))

    came_from = {}
    effect_so_far = {}
    visited = []
    came_from[start] = None
    effect_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]
        visited.append(current)
        current_room = get_state(current)
        if current_room['id'] == goal:
            print('Total Hp:',effect_so_far[current])
            break
        
        for i in range(len(current_room['neighbors'])):
            neighbor = current_room['neighbors'][i]['id']
            if neighbor not in visited:
                t_state = transition_state(current_room['id'],neighbor)
                new_effect = effect_so_far[current] + t_state['event']['effect']
                if neighbor not in effect_so_far or new_effect < effect_so_far[neighbor]:
                    effect_so_far[neighbor] = new_effect
                    priority = new_effect
                    came_from[neighbor] = current
                    frontier.put((priority,neighbor))

    current = goal 
    path = [current]
    while current != start: 
        current = came_from[current]
        path.append(current)
    path.reverse()
    
    print(path)    

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

if __name__ == "__main__":

    s_id = '7f3dc077574c013d98b2de8f735058b4'
    f_id = 'f1f131f647621a4be7c71292e79613f9'

    bfs(s_id,f_id)
    dijkstra(s_id,f_id)





