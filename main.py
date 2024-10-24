import algorithms.dfs
import states
import algorithms.bfs

states_object = states.States()
dfs = algorithms.dfs.DFS(867254301)
status = dfs.perform_iterative_DFS()
print(status)
path, cost, expanded, depth = dfs.get_results()
print(path)
print("cost = "+str(cost))
print("expanded = "+str(expanded))
print("depth = "+str(depth))
# print(states_object.check_goal(12345678))
# print(states_object.get_direction(52431876,452031876))
# print(states_object.get_next_state(52431876))

# bfs = algorithms.bfs.BFS(120345678)
# print(bfs.BFS())
# print(bfs.get_path())
# print(bfs.get_nodes_expanded())
# print(bfs.get_search_level())

