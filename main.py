import states
import algorithms.bfs

states_object = states.States()

print(states_object.check_goal(12345678))
print(states_object.get_direction(52431876,452031876))
print(states_object.get_next_state(52431876))

bfs = algorithms.bfs.BFS(867254301)
print(bfs.BFS())
print(bfs.get_path())
print(bfs.get_nodes_expanded())
print(len(bfs.get_nodes_expanded()))
print(bfs.get_search_level())
print(len(bfs.get_path()))
