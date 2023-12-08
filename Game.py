import Gamelogic
import copy
import random

# Method that returns board from Gamelogic
class Game:
    def __init__(self):
        self.board = Gamelogic.create_board()


    def get_value(self, x, y):
        return self.board[x][y]


    def place(self, x, y):
        if self.board[x][y] == 0:
           self.board[x][y] = 2
           return True
        else:
            return False
        

        
    def Shift_Right(self):
        for _ in range(3):
            for x in range(3):
                for y in range(4):
                    if self.board[x][y] == 0:
                        continue
                    if self.board[x+1][y] == 0:
                        self.board[x+1][y] = self.board[x][y]
                        self.board[x][y] = 0
            
    def combine_right(self):
        merged = [[False for _ in range(4)]for _ in range (4)]
        for x in range(3):
            for y in range(4):
                if self.board[x][y] == 0 or merged[x][y] == True or merged[x+1][y]:
                    continue
                if self.board[x+1][y] == self.board[x][y]:
                    self.board[x][y] = self.board[x][y]*2
                    self.board[x+1][y] = 0
                    merged[x][y] = True    

    def Shift_Left(self):
        for _ in range(3):
            for x in range(1,4):
                for y in range(4):
                    if self.board[x][y] == 0:
                        continue
                    if self.board[x-1][y] == 0:
                        self.board[x-1][y] = self.board[x][y]
                        self.board[x][y] = 0


    def combine_Left(self):
        merged = [[False for _ in range(4)]for _ in range (4)]
        for x in range(1,4):
            for y in range(4):
                if self.board[x][y] == 0 or merged[x][y] == True or merged[x-1][y]:
                    continue
                if self.board[x-1][y] == self.board[x][y]:
                    self.board[x][y] = self.board[x][y]*2
                    self.board[x-1][y] = 0
                    merged[x][y] = True

    def Shift_Up(self):
        for _ in range(3):
            for x in range(4):
                for y in range(1,4):
                    if self.board[x][y] == 0:
                        continue
                    if self.board[x][y-1] == 0:
                        self.board[x][y-1] = self.board[x][y]
                        self.board[x][y] = 0

    def combine_Up(self):
        merged = [[False for _ in range(4)]for _ in range (4)]
        for x in range(4):
            for y in range(1,4):
                if self.board[x][y] == 0 or merged[x][y] == True or merged[x][y-1]:
                    continue
                if self.board[x][y-1] == self.board[x][y]:
                    self.board[x][y] = self.board[x][y]*2
                    self.board[x][y-1] = 0
                    merged[x][y] = True


    def Shift_Down(self):
        for _ in range(3):
            for x in range(4):
                for y in range(3):
                    if self.board[x][y] == 0:
                        continue
                    if self.board[x][y+1] == 0:
                        self.board[x][y+1] = self.board[x][y]
                        self.board[x][y] = 0
        
    def combine_Down(self):
        merged = [[False for _ in range(4)]for _ in range (4)]
        for x in range(4):
            for y in range(3):
                if self.board[x][y] == 0 or merged[x][y] == True or merged[x][y+1]:
                    continue
                if self.board[x][y+1] == self.board[x][y]:
                    self.board[x][y] = self.board[x][y]*2
                    self.board[x][y+1] = 0
                    merged[x][y] = True


    def generate_new_sq(self):
        Full = False
        while not Full:
        #beginning to the loop. We don't know how many times we'll need it
            new_x = random.randint(0,3)
            new_y = random.randint(0,3)

                #Empty square
            if self.board[new_x][new_y] == 0:
                    #1 in 10 chance space = 4
                if random.randint(1,10) == 10:
                        self.board[new_x][new_y] = 4 
                else:    
                        self.board[new_x][new_y] = 2
                #Can place a 2 there
                Full = True
                    #Exit to the loop

    def checkforwin(self):
        directions = ['w', 'a', 's', 'd']
        for d in directions:
            temp_board = copy.deepcopy(self)
            self.move(temp_board, d)
            if temp_board != self.board:
                return False
        return True
        
    def move(self, direction):
        temp_board = copy.deepcopy(self.board)
        
        match direction:
            case 'w':
                self.Shift_Up()
                self.combine_Up()
                self.Shift_Up()
            case 'a':
                self.Shift_Left()
                self.combine_Left()
                self.Shift_Left()
            case 's':
                self.Shift_Down()
                self.combine_Down()
                self.Shift_Down()
            case 'd': 
                self.Shift_Right()
                self.combine_right()
                self.Shift_Right()
        
        if temp_board != self.board:
            self.generate_new_sq()        