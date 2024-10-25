from collections import defaultdict
import queue
import states
import algorithms.search_strategy as strat


class BFS(strat.SearchStrategy):
    def __init__(self, initialState):
        self.initialState = initialState
        self.parent = {}
        self.nodesExpanded = []
        self.stateObj = states.States()
        self.level = 0

    def execute(self):
        frontier = queue.Queue()
        explored = defaultdict(lambda: False)
        frontier.put((0 ,self.initialState))


        while not frontier.empty():
            state = frontier.get()
            explored[state[1]] = True
            self.nodesExpanded.append(state[1])

            if self.stateObj.check_goal(state[1]):
                self.level = state[0]
                return "success"

            nextStates = self.stateObj.get_next_state(state[1])
            for next_state in nextStates:
                if not explored[next_state]:                    
                    self.parent[next_state] = state[1]
                    frontier.put((state[0] + 1 , next_state))

        return "failed"

    def get_path(self):
        goalState = 12345678
        directions = []
        while goalState != self.initialState:
            direction = self.stateObj.get_direction(self.parent[goalState], goalState)
            directions.insert(0, (goalState, direction))
            goalState = self.parent[goalState]

        return directions

    def get_nodes_expanded(self):
        return self.nodesExpanded

    def get_search_level(self):
        return self.level
            

    def get_results(self):
        path = self.get_path()
        return path, len(path), len(self.get_nodes_expanded()), self.get_search_level()






