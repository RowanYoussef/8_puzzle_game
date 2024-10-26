import algorithms.search_strategy as strategy
import states


class DFS(strategy.SearchStrategy):
    def __init__(self, state):
        ## setting initial search state
        self.initial_state = state
        ## Other attributes to keep track of nodes expanded, path and depth
        self.setup()
    def setup(self):
        self.nodes_expanded = 0
        self.state_helper = states.States()
        self.family_map = {}
        self.max_level = 0


        

    def execute(self):
        ## init frontier stack and explored map
        frontier = []
        explored = set()
        in_frontier = {self.initial_state}
        ## add initial state
        frontier.append((self.initial_state, 0))
        

        while len(frontier) > 0:
            ## pop state and update attributes
            curr_state, curr_level = frontier.pop()
            explored.add(curr_state)
            self.max_level = max(self.max_level, curr_level)
            self.nodes_expanded += 1
            ## checks of gaol was reached
            if self.state_helper.check_goal(curr_state):
                return True
            ## add other states to frontier
            neighbours = self.state_helper.get_next_state(curr_state)
            for n in neighbours:
                if (not n in explored) and (not n in in_frontier):
                    self.family_map[n] = curr_state
                    frontier.append((n, curr_level+1))
                    in_frontier.add(n)
                    
        return False
    
    def get_results(self):
        ## return the required results : path, cost, nodes expanded, depth
        path = []
        head_state = 12345678
        cost = 0
        while head_state != self.initial_state:
            cost += 1
            direction = self.state_helper.get_direction(self.family_map[head_state], head_state)
            path.append((head_state, direction))
            head_state = self.family_map[head_state]

        return path[::-1], cost, self.nodes_expanded, self.max_level
        