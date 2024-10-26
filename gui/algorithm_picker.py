import customtkinter as ctk


class AlgorithPicker(ctk.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.master = master
       # Dropdown input for "Search Method"
        self.search_method_label = ctk.CTkLabel(master, text="Search Method" ,font=("Arial", 20))
        self.search_method_label.grid(row=0, column=0, padx=10, pady=5, sticky="se")
            
        self.search_method_dropdown = ctk.CTkComboBox(master, values=["bfs", "dfs", "ids", "a_star_e", "a_star_m"])
        self.search_method_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="s")