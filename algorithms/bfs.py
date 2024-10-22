from collections import defaultdict, deque
import queue
import states


class BFS:
    def __init__(self, initiaState):
        self.intialState = initiaState
        self.parent = {}
        self.cost = 0
        self.level = 0
        self.nodesExpanded = []
        self.stateObj = states.States()
    
    def BFS(self):
        frontier = queue.Queue()
        explored = defaultdict(lambda:False)
        frontier.put(self.intialState)

        while not frontier.empty():
            state = frontier.get()
            explored[state] = True
            self.nodesExpanded.append((state))

            if self.stateObj.check_goal(state):
                return "success"
            
            nextStates = self.stateObj.get_next_state(state)
            if nextStates != []:
                self.level += 1
                for i in range(len(nextStates)):
                    if explored[nextStates[i]] == False:
                        self.parent[nextStates[i]] = state
                        frontier.put(nextStates[i])

        return "failed"
    
    def get_path(self):
        goalState = 12345678
        directions = []
        while goalState != self.intialState:
            self.cost += 1
            direction = self.stateObj.get_direction(self.parent[goalState] , goalState)
            directions.insert(0 , direction)
            goalState = self.parent[goalState]
        
        return directions,self.cost
    
    def get_nodes_expanded(self):
        return self.nodesExpanded
    
    def get_search_level(self):
        return self.level
            








