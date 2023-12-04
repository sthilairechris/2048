import copy
import random

def game():
    input('Press Enter to Continue')
    board = create_board()
    #catching the return board from def create_board
    gamerunning = True
    while gamerunning:
        print_board(board)
        direction = get_user_input()
        if direction == 'x':
            gamerunning = False
        move(board, direction)
        checkforwin(board)

        #Checkforloss

def get_user_input():
    while True:
        valid_directions = ['w','a','s','d','x']
        direction = input('Choose direction using W,A,S,D')
        if direction in valid_directions:
    
            return direction
    


def place(board, x, y):
        if board[x][y] == 0:
            board[x][y] = 2
            return True
        else:
            return False
        


    
def Shift_Right(board):
    for _ in range(3):
        for x in range(3):
            for y in range(4):
             if board[x][y] == 0:
                continue
             if board[x+1][y] == 0:
                board[x+1][y] = board[x][y]
                board[x][y] = 0
            
def combine_right(board):
    merged = [[False for _ in range(4)]for _ in range (4)]
    for x in range(3):
        for y in range(4):
            if board[x][y] == 0 or merged[x][y] == True or merged[x+1][y]:
                continue
            if board[x+1][y] == board[x][y]:
                board[x][y] = board[x][y]*2
                board[x+1][y] = 0
                merged[x][y] = True

def Shift_Left(board):
    for _ in range(3):
        for x in range(1,4):
            for y in range(4):
                if board[x][y] == 0:
                    continue
                if board[x-1][y] == 0:
                    board[x-1][y] = board[x][y]
                    board[x][y] = 0


def combine_Left(board):
    merged = [[False for _ in range(4)]for _ in range (4)]
    for x in range(1,4):
        for y in range(4):
            if board[x][y] == 0 or merged[x][y] == True or merged[x-1][y]:
                continue
            if board[x-1][y] == board[x][y]:
                board[x][y] = board[x][y]*2
                board[x-1][y] = 0
                merged[x][y] = True


def Shift_Up(board):
    for _ in range(3):
        for x in range(4):
            for y in range(1,4):
                if board[x][y] == 0:
                    continue
                if board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0

def combine_Up(board):
    merged = [[False for _ in range(4)]for _ in range (4)]
    for x in range(4):
        for y in range(1,4):
            if board[x][y] == 0 or merged[x][y] == True or merged[x][y-1]:
                continue
            if board[x][y-1] == board[x][y]:
                board[x][y] = board[x][y]*2
                board[x][y-1] = 0
                merged[x][y] = True
             

def Shift_Down(board):
    for _ in range(3):
        for x in range(4):
            for y in range(3):
                if board[x][y] == 0:
                    continue
                if board[x][y+1] == 0:
                    board[x][y+1] = board[x][y]
                    board[x][y] = 0
        
def combine_Down(board):
    merged = [[False for _ in range(4)]for _ in range (4)]
    for x in range(4):
        for y in range(3):
            if board[x][y] == 0 or merged[x][y] == True or merged[x][y+1]:
                continue
            if board[x][y+1] == board[x][y]:
                board[x][y] = board[x][y]*2
                board[x][y+1] = 0
                merged[x][y] = True
                
def checkforwin(board):
    directions = ['w', 'a', 's', 'd']
    for d in directions:
        temp_board = copy.deepcopy(board)
        move(temp_board, d)
        if temp_board != board:
            return False
    return True

def move(board, direction):
    temp_board = copy.deepcopy(board)
    
    match direction:
        case 'w':
            Shift_Up(board)
            combine_Up(board)
            Shift_Up(board)
        case 'a':
            Shift_Left(board)
            combine_Left(board)
            Shift_Left(board)
        case 's':
            Shift_Down(board)
            combine_Down(board)
            Shift_Down(board)
        case 'd': 
            Shift_Right(board)
            combine_right(board)
            Shift_Right(board)

    if temp_board != board:
        generate_new_sq(board)


def create_board():
    ys, xs = (4, 4)
    board = [[0 for i in range(xs)] for j in range(ys)]
    generate_new_sq(board)
    generate_new_sq(board)
    
    return board

def print_board(board):
    print(board)
    print('\n'*3)
    #Add print numbers
    #Use braces to get value from variable
    print('-' *25)
    print('|     |     |     |     |')
    print(f'| {board[0][0]}   | {board[1][0]}   | {board[2][0]}   | {board[3][0]}   |') 
    #Where the functions are able to be input
    print('|     |     |     |     |')
    print('-' *25)
    print('|     |     |     |     |')
    print(f'| {board[0][1]}   | {board[1][1]}   | {board[2][1]}   | {board[3][1]}   |')
    print('|     |     |     |     |')
    print('-' *25)
    print('|     |     |     |     |')
    print(f'| {board[0][2]}   | {board[1][2]}   | {board[2][2]}   | {board[3][2]}   |')
    print('|     |     |     |     |')
    print('-' *25)
    print(f'| {board[0][3]}   | {board[1][3]}   | {board[2][3]}   | {board[3][3]}   |')
    print('|     |     |     |     |')
    print('-' *25)

def flatten_board(board):
    flat_board = []
    for row in board:
        for sq in row:
           flat_board.append(sq) 
    return flat_board


def generate_new_sq(board):
    Full = False
    while not Full:
    #beginning to the loop. We don't know how many times we'll need it
        new_x = random.randint(0,3)
        new_y = random.randint(0,3)
    
            #Empty square
        if board[new_x][new_y] == 0:
                #1 in 10 chance space = 4
            if random.randint(1,10) == 10:
                    board[new_x][new_y] = 4 
            else:    
                    board[new_x][new_y] = 2
            #Can place a 2 there
            Full = True
                #Exit to the loop


