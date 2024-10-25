
import customtkinter
from context import Context
from gui.mainframe import MainFrame
# 120345678 -> 2
# 123456078 -> 22
# 874012356 -> 19
# 123450786 -> 21
# 136502478 -> 22
# 236158407 -> 23
# 876543210 -> 28
# 102754863 -> 23
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x900")
        self.title("8 Puzzle Game")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MainFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # add widgets to app
        


app = App()
app.mainloop()

ctx = Context()
ctx.set_strat('ids')
#search = ctx.get_strat_obj(120345678)
#search = ctx.get_strat_obj(123456078)
#search = ctx.get_strat_obj(874012356)
#search = ctx.get_strat_obj(123450786)
#search = ctx.get_strat_obj(136502478)
#search = ctx.get_strat_obj(236158407)
# search = ctx.get_strat_obj(876543210)
# #search = ctx.get_strat_obj(102754863)
# success = search.execute()
# if success:
#     print("success")
#     p, c, n, l = search.get_results()
#     print(p)
#     print("cost " + str(c))
#     print("expanded "+str(n))
#     print("depth " + str(l))
# else:
#     print("ids")





