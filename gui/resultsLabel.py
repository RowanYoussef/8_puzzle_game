import customtkinter as ctk


class Results(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.master = master

        # Labels for displaying time, depth, cost, and expanded nodes
        self.time_label = ctk.CTkLabel(master, text=f"Time: 0.0 ms",font=("Arial", 16))
        self.time_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        self.depth_label = ctk.CTkLabel(master, text=f"Depth: 0",font=("Arial", 16))
        self.depth_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        self.cost_label = ctk.CTkLabel(master, text=f"Cost: 0",font=("Arial", 16))
        self.cost_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        self.expanded_label = ctk.CTkLabel(master, text=f"Expanded Nodes: 0",font=("Arial", 16))
        self.expanded_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")