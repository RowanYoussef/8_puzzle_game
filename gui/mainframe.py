import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0,1,2), weight=1)
        
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        # 1. Dropdown input for "Search Method"
        self.search_method_label = ctk.CTkLabel(self, text="Search Method")
        self.search_method_label.grid(row=0, column=0, padx=10, pady=5, sticky="se")
        
        self.search_method_dropdown = ctk.CTkComboBox(self, values=["bfs", "dfs", "ids", "a_star_e", "a_star_m"])
        self.search_method_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="s")
        
        # 2. Number input field for "Sample"
        self.sample_label = ctk.CTkLabel(self, text="Sample")
        self.sample_label.grid(row=1, column=0, padx=10, pady=5, sticky="se")
        
        self.sample_input = ctk.CTkEntry(self, width=100)
        self.sample_input.grid(row=1, column=1, padx=10, pady=5, sticky="s")
        
        # 3. 3x3 Grid Output for 9-digit number input
        self.grid_output_label = ctk.CTkLabel(self, text="Grid Output")
        self.grid_output_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.grid_frame = ctk.CTkFrame(self, width=400, height=400)
        self.grid_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.grid_cells = [[ctk.CTkLabel(self.grid_frame, text="", fg_color="white", width=100, height=100) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid_cells[i][j].grid(padx=2, pady= 2,row=i, column=j)
        
        self.status_label = ctk.CTkLabel(self, text="Has not Started")
        self.status_label.grid(row=3, column=0, padx=10, pady=5, sticky="se")

        # Button to update grid based on number input
        self.grid_button = ctk.CTkButton(self, text="Start", command=self.update_grid)
        self.grid_button.grid(row=3, column=1, padx=10, pady=5, sticky="s")
        
        # 4. Label with "Prev" and "Next" buttons
        self.navigation_frame = ctk.CTkFrame(self)
        self.navigation_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        self.prev_button = ctk.CTkButton(self.navigation_frame, text="Prev", command=self.prev_string)
        self.prev_button.grid(row=5, column=0, padx=5)
        
        self.string_label = ctk.CTkLabel(self.navigation_frame, text="Direction")
        self.string_label.grid(row=5, column=1, padx=5)
        
        self.next_button = ctk.CTkButton(self.navigation_frame, text="Next", command=self.next_string)
        self.next_button.grid(row=5, column=2, padx=5)

        # Label for Nodes Expanded
        self.nodes_expanded_label = ctk.CTkLabel(self, text="Nodes Expanded:")
        self.nodes_expanded_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        
        self.nodes_expanded_value = ctk.CTkLabel(self, text="0")
        self.nodes_expanded_value.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        
        # Label for Time
        self.time_label = ctk.CTkLabel(self, text="Time:")
        self.time_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        
        self.time_value = ctk.CTkLabel(self, text="0.0s")
        self.time_value.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        
        # Label for Cost
        self.cost_label = ctk.CTkLabel(self, text="Cost:")
        self.cost_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        
        self.cost_value = ctk.CTkLabel(self, text="0")
        self.cost_value.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        
        # Label for Depth
        self.depth_label = ctk.CTkLabel(self, text="Depth:")
        self.depth_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        
        self.depth_value = ctk.CTkLabel(self, text="0")
        self.depth_value.grid(row=9, column=1, padx=10, pady=5, sticky="w")

        # Sample data for dynamic label updates
        self.strings = [""]
        self.current_index = 0

    def update_grid(self):
        # Get the sample input and convert it into a grid
        sample_value = self.sample_input.get()
        
        if len(sample_value) == 9 and sample_value.isdigit():
            for i in range(3):
                for j in range(3):
                    self.grid_cells[i][j].configure(text=sample_value[i*3 + j])
        else:
            # Display error or clear grid if input is invalid
            for row in self.grid_cells:
                for cell in row:
                    cell.configure(text="")

    def prev_string(self):
        # Show previous string in the list
        self.current_index = (self.current_index - 1) % len(self.strings)
        self.string_label.configure(text=self.strings[self.current_index])

    def next_string(self):
        # Show next string in the list
        self.current_index = (self.current_index + 1) % len(self.strings)
        self.string_label.configure(text=self.strings[self.current_index])