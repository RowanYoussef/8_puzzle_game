import customtkinter as ctk


class SampleField(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.master = master
        # Number input field for "Sample"
        self.sample_label = ctk.CTkLabel(master, text="Sample" , font=("Arial", 20))
        self.sample_label.grid(row=1, column=0, padx=10, pady=5, sticky="se")
        
        self.sample_input = ctk.CTkEntry(master, width=100)
        self.sample_input.grid(row=1, column=1, padx=10, pady=5, sticky="s")

