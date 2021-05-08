import numpy as np
Forward_Backward = [(1,0),(0,1),(-1,0),(0,-1)]
Diagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

class Piece:
    
    def __init__(self, x, y):
        self.x = None
        self.y = None
    
    def Check(x,y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
    
    def Move(self,x,y,directions):
        Position =[]
        for x_dir,y_dir in directions:
            x_aux, y_aux = x + x_dir, y + y_dir
            while self.Check(x_aux,y_aux):
                Position.append((x_aux,y_aux))
                x_aux, y_aux = x_aux + x_dir, y_aux + y_dir
        return Position
    
    def Draw(x,y,Position):
        Board = np.zeros((8, 8))
        Board[x][y] = 8
        for a,b in Position:
                Board[a][b]=1
        return Board


#if __name__ == "__main__":
    
        #import numpy as np 
    #x=4
    #y=3
    #Position = Piece.Move(Piece,x,y, Diagonals+Forward_Backward)
    #print(Piece.Draw(x,y, Position))