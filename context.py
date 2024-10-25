import algorithms.dfs as dfs
import algorithms.bfs as bfs
import algorithms.ids as ids
import algorithms.a_star as a_star
class Context:
    def __init__(self):
        self.strat = 'dfs'
    
    def set_strat(self, strat):
        self.strat = strat
    
    def get_strat_obj(self, state):
        val = self.strat
        if val == "dfs":
            return dfs.DFS(state)
        elif val == "bfs":
            return bfs.BFS(state)
        elif val == "ids":
            return ids.IDS(state)
        elif val == "a_star_e":
            return a_star.AStar(state, "euclidean")
        else:
            return a_star.AStar(state, "manhattan")