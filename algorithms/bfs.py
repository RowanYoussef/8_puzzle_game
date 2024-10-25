from collections import defaultdict
import queue
import states
import algorithms.search_strategy as strat


class BFS(strat.SearchStrategy):
    def __init__(self, initialState):
        #init initial state ,parent map , stateobject and level
        self.initialState = initialState
        self.parent = {}
        self.nodesExpanded = []
        self.stateObj = states.States()
        self.level = 0

    def execute(self):
        #init frontier and explored set
        frontier = queue.Queue()
        explored = set()
        in_frontier = {self.initialState}
        frontier.put((0 ,self.initialState))

        #check if there is any state to visit
        while not frontier.empty():
            state = frontier.get()
            in_frontier.remove(state[1])
            explored.add(state[1])
            self.nodesExpanded.append(state[1])
            
            #check if the goal is reached
            if self.stateObj.check_goal(state[1]):
                self.level = state[0]
                return "success"
            
            #get neighbours state of the current state
            nextStates = self.stateObj.get_next_state(state[1])
            for next_state in nextStates:
                #check if the state is valid
                if (not next_state in in_frontier) and (not next_state in explored):                    
                    self.parent[next_state] = state[1]
                    #increase the level
                    frontier.put((state[0] + 1 , next_state))
                    in_frontier.add(next_state)

        return "failed"

    #function to get the path from the parent list
    def get_path(self):
        goalState = 12345678
        directions = []
        while goalState != self.initialState:
            direction = self.stateObj.get_direction(self.parent[goalState], goalState)
            directions.insert(0, (goalState, direction))
            goalState = self.parent[goalState]

        return directions

    #get nodes expanded
    def get_nodes_expanded(self):
        return self.nodesExpanded

    #get level
    def get_search_level(self):
        return self.level
            
    #get all the privious results
    def get_results(self):
        path = self.get_path()
        return path, len(path), len(self.get_nodes_expanded()), self.get_search_level()






