    # def start_callback(self):
    #     # Update state
    #     self.status_label.configure(text="Loading")
        
    #     initial_state = self.input_text.sample_input.get()
    #     # Perform the long-running task
    #     self.board.update_grid(initial_state)
    #     algorithm = self.search_method.search_method_dropdown.get()
    #     self.ctx.set_strat(algorithm)
    #     search = self.ctx.get_strat_obj(int(initial_state))   
    #     # Once done, you can update the status again if needed
    #     self.status_label.configure(text="Finished")
    #     self.path , self.cost , self.expanded , self.depth = search.get_results()