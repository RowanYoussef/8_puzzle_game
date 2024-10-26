
import customtkinter
from gui.mainframe import MainFrame

#main window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x900")
        self.title("8 Puzzle Game")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MainFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        


app = App()
app.mainloop()





