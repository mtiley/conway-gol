# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:28:43 2019

@author: miles
"""
            
class cell:
    ## each cell is one 'pixel' in the game whose state can be either ON (1) or 
    ## OFF (0)
    def __init__(self, xpos, ypos, state):
        self.xpos = xpos 
        self.ypos = ypos
        self.state = state
        self.count = 0
        
        
class universe:
    def __init__(self, size, pr = [0.5, 0.5], seed = None):
        self.size = size
        self.pr = pr
        self.seed = seed
        self.cells = np.empty((size,size), dtype=cell)
        
        np.random.seed(self.seed)
        print(f"Universe initialised with seed = [{self.seed}] (ignore outer brackets)")
        self.states = np.random.choice(2, size=(size,size), p = pr)

        for row in range(size):
            for col_pos in range(size):
                self.cells[row][col_pos]=(cell(col_pos, row, self.states[row][col_pos]))
            
    def cell_count(self):
        for row in range(self.size):
            for col in range(self.size):
                self.cells[row][col].count = (self.cells[row-1][col-1].state + ## need to implement rolling so can look at 'other side' of array
                            self.cells[row-1][col].state +
                            self.cells[row][col-1].state +
                            self.cells[row][col+1].state +
                            self.cells[row+1][col-1].state +
                            self.cells[row+1][col].state +
                            self.cells[row-1][col-1].state +
                            self.cells[row+1][col+1].state)


u1 = universe(20, seed =111)
print(u1.states)
u1.cell_count()                                
#print(u1.cells[1][0].state)
print("count = ", u1.cells[0][0].count)
      
        