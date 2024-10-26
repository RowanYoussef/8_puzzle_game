import customtkinter as ctk
from .algorithm_picker import AlgorithPicker
from .sample_field import SampleField
from .board import Board
import threading
from context import Context
from datetime import datetime
from .resultsLabel import Results

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Dropdown input for "Search Method"
        self.search_method = AlgorithPicker(self)

        # Number input field for "Sample"
        self.input_text = SampleField(self)

        # 3x3 Grid Output for 9-digit number input
        self.board = Board(self)
        self.status_label = ctk.CTkLabel(self, text="Has not Started" ,font=("Arial", 20))
        self.status_label.grid(row=3, column=0, padx=10, pady=5, sticky="se")

        # Button to update grid based on number input
        self.grid_button = ctk.CTkButton(self, text="Start", font=("Arial", 20),command=self.start_thread)
        self.grid_button.grid(row=3, column=1, padx=10, pady=5, sticky="s")

        # Label with "Prev" and "Next" buttons
        self.navigation_frame = ctk.CTkFrame(self)
        self.navigation_frame.grid(row=4, column=0, columnspan=3, pady=10)

        self.prev_button = ctk.CTkButton(self.navigation_frame, text="Prev", command=self.get_prev_state)
        self.prev_button.grid(row=5, column=0, padx=5)

        self.string_label = ctk.CTkLabel(self.navigation_frame, text="Direction")
        self.string_label.grid(row=5, column=1, padx=5)

        self.next_button = ctk.CTkButton(self.navigation_frame, text="Next", command=self.get_next_state)
        self.next_button.grid(row=5, column=2, padx=5)

        self.results = Results(self)

        # Initialize variables
        self.path = []
        self.cost = 0
        self.expanded = 0
        self.depth = 0
        self.index = -1
        self.initial_state = 0
        self.time = 0
        self.ctx = Context()

    def start_thread(self):
        # Create and start a thread for running the task
        thread = threading.Thread(target=self.start_callback)
        thread.start()

    def start_callback(self):
        self.path = []
        self.cost = 0
        self.expanded = 0
        self.depth = 0
        self.index = -1
        self.time = 0
       
        #reset results
        self.results.time_label.configure(text=f"Time: 0.0 ms")
        self.status_label.configure(text="Loading")
        self.string_label.configure(text="Direction")
        self.results.cost_label.configure(text=f"Cost: 0")
        self.results.depth_label.configure(text=f"Depth: 0")
        self.results.expanded_label.configure(text=f"Expanded Nodes: 0")
        
         # Update state
        self.initial_state = self.input_text.sample_input.get()
        
        # Perform the long-running task
        self.board.update_grid(self.initial_state)
        algorithm = self.search_method.search_method_dropdown.get()
        self.ctx.set_strat(algorithm)
        
        start_time = datetime.now()
        search = self.ctx.get_strat_obj(int(self.initial_state))   
        
        # Execute the search algorithm
        success = search.execute()
        
        end_time = datetime.now()
        time_difference = end_time - start_time
        milliseconds = time_difference.total_seconds() * 1000
        self.time = milliseconds

        # Update labels with results
        self.status_label.configure(text="Finished")
        self.results.time_label.configure(text=f"Time: {self.time:.2f} ms")
        if success:
            print("success")
            self.path, self.cost, self.expanded, self.depth = search.get_results()
            self.results.cost_label.configure(text=f"Cost: {self.cost}")
            self.results.depth_label.configure(text=f"Depth: {self.depth}")
            self.results.expanded_label.configure(text=f"Expanded Nodes: {self.expanded}")
        else:
            self.status_label.configure(text="Can't be solved")

    # Get next state in grid
    def get_next_state(self):
        if self.index + 1 < len(self.path):
            self.index += 1
            self.string_label.configure(text=self.path[self.index][1])
            state = self.path[self.index][0]
            self.board.update_grid(state) 

    # Get previous state in grid
    def get_prev_state(self):
        if self.index - 1 >= 0:
            self.index -= 1
            self.string_label.configure(text=self.path[self.index][1])
            state = self.path[self.index][0]
            self.board.update_grid(state)
        elif self.index - 1 == -1:
            self.index = -1
            self.board.update_grid(self.initial_state)
            self.string_label.configure(text="Direction")

            
        

