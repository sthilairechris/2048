x = 7 
y = 16
z = x
x = y

y = z

print(x)
print(y)


def Shift_left(board):
    for x in range(4):
        for y in range(4):
            shift = 0
            if x > 0: 
                #z is a placeholder for however many spaces are in the column
                for z in range(x):
                    if board[z][y] == 0:
                        #allows us to shift into whatever space = 0
                        shift += 1 
                        if shift > 0: 
                            if board[x - shift][y] == 0:
                                board[x - shift][y] = board[x][y]
                                board[x][y] = 0