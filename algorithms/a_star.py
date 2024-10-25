import heapq
from algorithms.heuristic_factory import HeuristicFactory
import states
import algorithms.search_strategy as strat
class AStar(strat.SearchStrategy):
    def __init__(self, initialState, heuristic_name):
        self.initialState = initialState
        self.heuristic_fn = HeuristicFactory.create_heuristic(heuristic_name)
        self.parents = {}
        self.nodesExpanded = []
        self.stateObj = states.States()
        self.level = 0
        self.cost = {} # state, cost  -> g(n) 

    def execute(self):
        frontier = []
        explored = set()
        
        heapq.heappush(frontier, (self.heuristic_fn(self.initialState), 0, self.initialState)) # f, g, state (sorts based on f)
        self.cost[self.initialState] = 0

        while frontier:
            f_val, g_val, state = heapq.heappop(frontier)
            explored.add(state)
            self.nodesExpanded.append(state)

            if self.stateObj.check_goal(state):
                self.level = g_val
                return "success"

            nextStates = self.stateObj.get_next_state(state)
            for next_state in nextStates:
                new_g = g_val + 1
                if next_state not in explored or new_g < self.cost.get(next_state, float('inf')): # if new_g is less than the current g cost of the state since the heuristic is the same
                    self.cost[next_state] = new_g
                    new_f = new_g + self.heuristic_fn(next_state)
                    heapq.heappush(frontier, (new_f, new_g, next_state))
                    self.parents[next_state] = state

        return "failed"

    def get_path(self):
        goalState = 12345678
        directions = []
        
        while goalState != self.initialState:
            direction = self.stateObj.get_direction(self.parents[goalState], goalState)
            directions.append((goalState, direction))
            goalState = self.parents[goalState]

        directions.reverse()
        return directions
    
    def get_nodes_expanded(self):
        return self.nodesExpanded

    def get_search_level(self):
        return self.level

    def get_results(self):
        path = self.get_path()
        return path, len(path), len(self.get_nodes_expanded()), self.get_search_level()
