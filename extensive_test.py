from itertools import permutations
from math import factorial

from algorithms import a_star, bfs



def is_solvable(state):
    state = str(state)
    if len(state) == 8:
        state = "0" + state
    inversions = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] != "0" and state[j] != "0" and int(state[i]) > int(state[j]):
                inversions += 1
    return inversions % 2 == 0



def generate_solvable_permutations():
    digits = '012345678'
    all_solvable_states = []
    
    # Generate all permutations of the digits '0' through '8'
    for perm in permutations(digits):
        state = ''.join(perm)
        
        # Check if the permutation is a solvable state
        if is_solvable(state):
            all_solvable_states.append(state)
    
    return all_solvable_states


solvable_states = generate_solvable_permutations()
print(f"Number of solvable states: {len(solvable_states)} (should be {factorial(9) // 2}((9!/2)))")



# test

for state in solvable_states:
    state = int(state)
    bfs_instance = bfs.BFS(state)
    bfs_instance.BFS()
    ans1 = bfs_instance.get_search_level()
    
    astar_instance = a_star.AStar(state, "manhattan")
    astar_instance.A_star()
    ans2 = astar_instance.get_search_level()
    
    a_star_instance2 = a_star.AStar(state, "euclidean")
    a_star_instance2.A_star()
    ans3 = a_star_instance2.get_search_level()
    
       
    
    
    assert ans1 == ans2 == ans3 # == ans4
    print("Test passed!")
print("All tests passed!")

