class States:
    stateMap = {
        0 : [1 , "right" , 3 , "buttom"],
        1 : [0 , "left" , 2 , "right" , 4 , "buttom"],
        2 : [1 , "left" , 5 , "buttom"],
        3 : [0 , "up" , 4 , "right" , 6 , "buttom"],
        4 : [1 , "up" , 3 , "left" , 5 , "right" , 7 , "buttom"],
        5 : [2 , "up" , 4 , "left" , 8 , "buttom"],
        6 : [3 , "up" , 7 , "right"],
        7 : [4 , "up" , 6 , "left" , 8 , "right"],
        8 : [5 , "up" , 7 , "left"]
    }

    def get_next_state(self , state):
        state_str = str(state)
        if len(state_str) == 8:
            state_str = "0" + state_str
        index = self.get_index_of_empty_slot(state_str)
        nextState = []
        for i in range(len(self.stateMap.get(index))):
            if i % 2 == 0:
                newString = self.swap(state_str , index , self.stateMap.get(index)[i])
                nextState.append(int(newString))
            else:
                nextState.append(self.stateMap.get(index)[i])
        return nextState
    

    def get_index_of_empty_slot(self,state_str):
        for i in range(len(state_str)):
            if state_str[i] == "0":
                return i
            
    def check_goal(self , state):
        if state == 12345678:
            return True
        return False
    
    def swap(self, state_str, index1, index2):
        state_list = list(state_str)
        temp = state_list[index1]
        state_list[index1] = state_list[index2]
        state_list[index2] = temp
        swapped_state_str = ''.join(state_list)
        return swapped_state_str
