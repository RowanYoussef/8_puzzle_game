from algorithms.a_star import AStar
import algorithms.dfs as dfs
import states
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


# 120345678 -> 2
# 123456078 -> 22
# 874012356 -> 19
# 123450786 -> 21
# 136502478 -> 22
# 236158407 -> 23
# 876543210 -> 28
# 102754863 -> 23
ctx = Context()
ctx.set_strat('ids')
#search = ctx.get_strat_obj(120345678)
#search = ctx.get_strat_obj(123456078)
#search = ctx.get_strat_obj(874012356)
#search = ctx.get_strat_obj(123450786)
#search = ctx.get_strat_obj(136502478)
#search = ctx.get_strat_obj(236158407)
#search = ctx.get_strat_obj(876543210)
search = ctx.get_strat_obj(102754863)
success = search.execute()
if success:
    print("success")
    #p, c, n, l = search.get_results()
    #print(p)
    #print("cost " + str(c))
    #print("expanded "+str(n))
    #print("depth " + str(l))
else:
    print("failed")





