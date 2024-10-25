class States:
    #state map to get the next valid move
    stateMap = {
        0 : [1 , 3 ],
        1 : [0 , 2 , 4],
        2 : [1 , 5 ],
        3 : [0 , 4 , 6],
        4 : [1 , 3 , 5 , 7],
        5 : [2 , 4 , 8],
        6 : [3 , 7],
        7 : [4 , 6  , 8],
        8 : [5 , 7]
    }

    #direction map for mapping each move to its direction
    directionMap = {
        (0, 1): "right", (0, 3): "down", (1, 0): "left", 
        (1, 2): "right", (1, 4): "down", (2, 1): "left",
        (2, 5): "down", (3, 0): "up", (3, 4): "right",
        (3, 6): "down", (4, 1): "up", (4, 3): "left",
        (4, 5): "right", (4, 7): "down", (5, 2): "up",
        (5, 4): "left", (5, 8): "down", (6, 3): "up",
        (6, 7): "right", (7, 4): "up", (7, 6): "left",
        (7, 8): "right", (8, 5): "up", (8, 7): "left"
    }

    def get_next_state(self , state):
        state_str = str(state)
        #add 0 if the zero is at the begining
        if len(state_str) == 8:
            state_str = "0" + state_str
        #get the index of 0 to know how yo move
        index = self.get_index_of_empty_slot(state_str)
        nextState = []
        for i in range(len(self.stateMap[index])):
            newString = self.swap(state_str , index , self.stateMap[index][i])
            nextState.append(int(newString))
        return nextState
    
    #function takes the previous state and current state to return the direction
    def get_direction(self ,state1 , state2):
        state1 = str(state1)
        state2 = str(state2)
        if len(state1) == 8:
            state1 = "0" + state1
        if len(state2) == 8:
            state2 = "0" + state2
        direction = []
        index1 = self.get_index_of_empty_slot(state1)
        index2 = self.get_index_of_empty_slot(state2)
        direction = (index1, index2)
        stateDir = self.directionMap.get(direction)
        return stateDir
    

    def get_index_of_empty_slot(self,state_str):
        for i in range(len(state_str)):
            if state_str[i] == "0":
                return i

    #check if the state is the goal state     
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
    

        
    def calc_manhattan_cost(self, state):
        state_str = self.get_string_state(state)
        cost = 0
        for i in range(len(state_str)):
            if state_str[i] == "0":
                continue
            x1, y1 = i % 3, i // 3
            x2, y2 = int(state_str[i]) % 3, int(state_str[i]) // 3
            cost += abs(x1 - x2) + abs(y1 - y2)
        return cost
    
    def calc_euclidean_cost(self, state):
        state_str = self.get_string_state(state)
        cost = 0
        for i in range(len(state_str)):
            if state_str[i] == "0":
                continue
            x1 = i % 3
            y1 = i // 3
            x2 = int(state_str[i]) % 3
            y2 = int(state_str[i]) // 3
            cost += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return cost
    
    def get_string_state(self, state):
        state_str = str(state)
        if len(state_str) == 8:
            state_str = "0" + state_str
        return state_str
