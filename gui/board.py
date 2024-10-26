import customtkinter as ctk

class Board(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # 3x3 Grid Output for 9-digit number input
        self.grid_output_label = ctk.CTkLabel(master, text="Grid Output", font=("Arial", 20))
        self.grid_output_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.grid_frame = ctk.CTkFrame(master, width=400, height=400)
        self.grid_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        font_size = 24  

        self.grid_cells = [
            [ctk.CTkLabel(self.grid_frame, text="", fg_color="white", width=100, height=100, font=("Arial", font_size)) for _ in range(3)]
            for _ in range(3)
        ]
        
        for i in range(3):
            for j in range(3):
                self.grid_cells[i][j].grid(padx=2, pady=2, row=i, column=j)

    def update_grid(self, sample_value):
        sample_value = str(sample_value)
        
        # Pad with leading zero if necessary to make it 9 digits
        if len(sample_value) == 8:
            sample_value = "0" + sample_value

        # Check for valid length and digits
        if len(sample_value) == 9 and sample_value.isdigit():
            # Check for duplicates
            if len(set(sample_value)) < 9:  
                print("Invalid input: Duplicate digits found.")
                for row in self.grid_cells:
                    for cell in row:
                        cell.configure(text="", fg_color="white") 
                return False
            else:
                self.strings = [sample_value]
                self.current_index = 0
                self.update_grid_display(sample_value)  
                return True
        else:
            for row in self.grid_cells:
                for cell in row:
                    cell.configure(text="", fg_color="white") 
            print("Invalid input: Please enter exactly 9 digits.")
            return False


    def update_grid_display(self, state):
        frame_color = self.grid_frame.cget("fg_color")
        for i in range(3):
            for j in range(3):
                value = state[i * 3 + j]
                if value == '0':  
                    self.grid_cells[i][j].configure(text="", fg_color=frame_color)  
                else:
                    self.grid_cells[i][j].configure(text=value, fg_color="white") 



