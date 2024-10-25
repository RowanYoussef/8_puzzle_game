from algorithms.a_star import AStar
import algorithms.dfs
import states
import algorithms.bfs

# states_object = states.States()
# dfs = algorithms.dfs.DFS(12345678)
# status = dfs.perform_iterative_DFS()
# print(status)
# path, cost, expanded, depth = dfs.get_results()
# print(path)
# print("cost = "+str(cost))
# print("expanded = "+str(expanded))
# print("depth = "+str(depth))
# print(states_object.check_goal(12345678))
# print(states_object.get_direction(52431876,452031876))
# print(states_object.get_next_state(52431876))

# bfs = algorithms.bfs.BFS(321645780)
# print(bfs.BFS())
# print(bfs.get_path())
# print(bfs.get_nodes_expanded())
# print(len(bfs.get_nodes_expanded()))
# print(bfs.get_search_level())
astar = AStar(312645780, "manhattan")
print(astar.A_star())
print(astar.get_path())
print(astar.get_nodes_expanded())
print(len(astar.get_nodes_expanded()))
print(astar.get_search_level())




