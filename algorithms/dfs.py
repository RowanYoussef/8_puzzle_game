from collections import defaultdict

import states


class DFS:
    def __init__(self, state):
        print("init")
        ## setting initial search state
        self.initial_state = state
        ## Other attributes to keep track of nodes expanded, path and depth
        self.nodes_expanded = 0
        self.state_helper = states.States()
        self.family_map = {}
        self.max_level = 0
    
    def perform_iterative_DFS(self):
        limit = 0
        val = self.perform_DFS(limit)
        while not val and limit <= 50:
            limit += 1
            val = self.perform_DFS(limit)
        return val
        

    def perform_DFS(self, limit = None):
        ## init frontier stack and explored map
        frontier = []
        explored = defaultdict(lambda: False)
        ## add initial state
        frontier.append((self.initial_state, 0))
        

        while len(frontier) > 0:
            ## pop state and update attributes
            curr_state, curr_level = frontier.pop()
            explored[curr_state] = True
            self.max_level = max(self.max_level, curr_level)
            self.nodes_expanded += 1
            print(str(curr_state) + " " + str(curr_level))
            ## checks of gaol was reached
            if self.state_helper.check_goal(curr_state):
                return True
            ## determine whether to continue deepening or not
            cont = True if limit == None else (True if limit >= curr_level+1 else False)
            if cont:
                ## add other states to frontier
                neighbours = self.state_helper.get_next_state(curr_state)
                for n in neighbours:
                    if not explored[n]:
                        self.family_map[n] = curr_state
                        frontier.append((n, curr_level+1))
        return False
    
    def get_results(self):
        ## return the required results : path, cost, nodes expanded, depth
        path = []
        head_state = 12345678
        cost = 0
        while head_state != self.initial_state:
            cost += 1
            direction = self.state_helper.get_direction(self.family_map[head_state], head_state)
            head_state = self.family_map[head_state]
            path.append((head_state, direction))

        return path[::-1], cost, self.nodes_expanded, self.max_level
        