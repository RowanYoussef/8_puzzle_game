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
print(states_object.check_goal(12345678))
print(states_object.get_direction(52431876,452031876))
print(states_object.get_next_state(52431876))

# bfs = algorithms.bfs.BFS(120345678)
# print(bfs.BFS())
# print(bfs.get_path())
# print(bfs.get_nodes_expanded())
# print(bfs.get_search_level())
# import pygame
# import states  # Your custom module for puzzle states
# import algorithms.bfs  # Your BFS algorithm implementation

# # Constants for GUI
# SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
# TILE_SIZE = 150
# FONT_SIZE = 75
# BACKGROUND_COLOR = (50, 50, 50)  # Dark gray background
# TILE_COLOR = (255, 255, 255)  # White tiles
# FONT_COLOR = (0, 0, 0)  # Black text on tiles
# BORDER_COLOR = (0, 0, 0)  # Black borders around tiles

# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("8 Puzzle Game")
# font = pygame.font.Font(None, FONT_SIZE)
# final_text_font = pygame.font.Font(None, 30)  # Smaller font for final text

# # Initialize your puzzle state
# initial_state = 123405678 # Replace this with the starting state of your puzzle
# states_object = states.States()
# bfs = algorithms.bfs.BFS(initial_state)

# # Perform BFS and check for success
# result = bfs.BFS()
# if result != "success":
#     print("BFS failed to find a solution.")
#     pygame.quit()
#     exit()

# # Render the puzzle state
# def draw_puzzle(state, direction=None):
#     state_str = str(state).zfill(9)  # Pad with zeros if necessary
#     for i in range(9):
#         x = (i % 3) * TILE_SIZE + (SCREEN_WIDTH - 3 * TILE_SIZE) // 2  # Center horizontally
#         y = (i // 3) * TILE_SIZE + (SCREEN_HEIGHT - 3 * TILE_SIZE) // 2  # Center vertically
#         if state_str[i] == '0':  # Blank tile
#             continue
#         # Draw tile background
#         pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
#         # Draw tile border
#         pygame.draw.rect(screen, BORDER_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 2)
#         # Draw the number in the center of the tile
#         text = font.render(state_str[i], True, FONT_COLOR)
#         screen.blit(text, (x + (TILE_SIZE - font.size(state_str[i])[0]) // 2,
#                              y + (TILE_SIZE - font.size(state_str[i])[1]) // 2))

#     # Draw the direction above the puzzle
#     if direction is not None:
#         direction_text = final_text_font.render(f"Direction: {direction}", True, FONT_COLOR)
#         screen.blit(direction_text, (10, 10))  # Display direction at the top of the screen

# # Function to wrap text to fit within a specified width
# def wrap_text(text, max_width):
#     """Wrap text to fit within a specified width."""
#     lines = []
#     words = text.split(' ')
#     current_line = ""

#     for word in words:
#         test_line = current_line + word + " "
#         if final_text_font.size(test_line)[0] <= max_width:
#             current_line = test_line
#         else:
#             lines.append(current_line)
#             current_line = word + " "

#     if current_line:
#         lines.append(current_line)

#     return lines

# # Main loop for GUI
# def game_loop(path):
#     running = True
#     state_index = 0  # Start at the first state
#     state_count = len(path)  # Total number of states
    
#     draw_puzzle(initial_state)
#     pygame.display.flip()
#     pygame.time.delay(1000)
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Check if there are states left to display
#         if state_index < state_count:
#             # Get the current state
#             current_state = path[state_index][0]
#             if state_index == 0:
#                 current_direction = ""
#             else:
#                 current_direction = path[state_index ][1]

#             # Clear the screen
#             screen.fill(BACKGROUND_COLOR)

#             # Draw the current puzzle state with the direction
#             draw_puzzle(current_state, current_direction)

#             # Display the puzzle grid
#             pygame.display.flip()

#             # Wait for 1 second before moving to the next state
#             pygame.time.delay(1000)

#             # Move to the next state
#             state_index += 1
#         else:
#             # All states have been displayed; proceed to results
#             show_final_results()

#             # Don't exit the loop; wait for the user to close
#             while running:
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         running = False

#     # Quit Pygame
#     pygame.quit()

# def show_final_results():
#     # Clear the screen
#     screen.fill(BACKGROUND_COLOR)

#     # Get additional data
#     path = bfs.get_path()
#     directions = []
#     for p in path:
#        directions.append(p[1])
#     cost = len(path)  
#     search_depth = bfs.get_search_level()
#     nodes_expanded = len(bfs.get_nodes_expanded())

#     # Prepare results including the wrapped path
#     results_texts = [
#         f"Cost: {cost}",
#         f"Search Depth: {search_depth}",
#         f"Nodes Expanded: {nodes_expanded}",
#     ]

#     # Wrap the path to fit the screen width
#     wrapped_path = wrap_text(f"Path: {' -> '.join(directions)}", SCREEN_WIDTH - 20)  # 20 for padding
#     results_texts.extend(wrapped_path)  # Add wrapped path lines

#     # Scroll settings
#     max_displayed_lines = (SCREEN_HEIGHT - 30) // 40  # Adjust this based on your screen and font size
#     scroll_position = 0  

#     while True:
#         # Clear the screen for each frame
#         screen.fill(BACKGROUND_COLOR)

#         # Render only a limited number of lines based on scroll position
#         for i in range(scroll_position, min(scroll_position + max_displayed_lines, len(results_texts))):
#             rendered_text = final_text_font.render(results_texts[i], True, FONT_COLOR)
#             screen.blit(rendered_text, (10, 30 + (i - scroll_position) * 40))

#         # Update the display
#         pygame.display.flip()

#         # Handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return  # Exit the function
            
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     if scroll_position < len(results_texts) - max_displayed_lines:
#                         scroll_position += 1  # Scroll down
#                 elif event.key == pygame.K_UP:
#                     if scroll_position > 0:
#                         scroll_position -= 1  # Scroll up

#         # Add a small delay to make scrolling manageable
#         pygame.time.delay(100)

# # Get the path (list of states) from the BFS algorithm
# path = bfs.get_path()

# # Run the game loop with the state list and directions
# game_loop(path)

# # Quit Pygame
# pygame.quit()

