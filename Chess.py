from Piece import Piece
Forward_Backward = [(1,0),(0,1),(-1,0),(0,-1)]
Diagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

class Tower:
    def Positions(self,x,y):
        Position = self.Move(self,x, y, Forward_Backward)
        return self.Draw(x,y,Position)

class Bishop:
    def Positions(self,x,y):
        Position = self.Move(self,x, y, Diagonals)
        return self.Draw(x,y,Position)

class Queen:
    def Positions(self,x,y):
        Position = self.Move(self,x, y, Forward_Backward+Diagonals)
        return self.Draw(x,y,Position)

class King:
    def Positions(self,x,y):
        King_Pos = [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]
        Position = []
        for p,q in King_Pos:
            if self.Check(p,q):
                Position.append((p,q))
        return self.Draw(x,y,Position)

class Horse:
    def Positions(self,x,y):
        cd1=1
        cd2=2
        Horse_Pos = [(x+cd1,y+cd2),(x-cd1,y+cd2),(x+cd1,y-cd2),(x-cd1,y-cd2),
                     (x+cd2,y+cd1),(x-cd2,y+cd1),(x+cd2,y-cd1),(x-cd2,y-cd1)]
        Position = []
        for p,q in Horse_Pos:
            if self.Check(p,q):
                Position.append((p,q))
        return self.Draw(x,y,Position)


if __name__ == "__main__":
    x = 3
    y = 4
    print('Tower')
    print(Tower.Positions(Piece,x,y))
    print('Bishop')
    print(Bishop.Positions(Piece,x,y))
    print('Queen')
    print(Queen.Positions(Piece,x,y))
    print('King')
    print(King.Positions(Piece,x,y))
    print('Horse')
    print(Horse.Positions(Piece,x,y))