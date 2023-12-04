import pygame
import Gamelogic



board = Gamelogic.create_board()



pygame.init()
font = pygame.font.Font("freesansbold.ttf", 20)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2048')


run = True

colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121), 
          16: (245, 149, 99), 
          32: (246, 124, 95), 
          64: (246, 94, 59), 
          128: (237, 207, 114),
          256: (237, 204, 97), 
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101), 
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

board_values = [[0 for _ in range(4) for _ in range(4)]]

def render_board(screen, board):
    square_width = 60
    for x in range(4):
        for y in range(4):
            pygame.draw.rect(screen, colors[board[x][y]], pygame.Rect((30 + square_width) * x +50, (30 + square_width) * y + 50, square_width, square_width), 0, 5)
            text_values = font.render(f'{board[x][y]}', 1, (0,0,0))
            screen.blit(text_values, ((30 + square_width) * x +50 + square_width / 2, (30 + square_width) * y + 50 + square_width / 2))


#def square_values(board):
#        for x in range(4):
#            for y in range(4):
#            value = board[x][y]
#            if value > 8:
#                    Value_color = colors['light text']
#            else:
#                Value_color = colors['dark text']
#            if value <= 2048:
#                color = colors[value]  
#            else: 
#                color = colors['other']

while run:

    render_board(screen, board)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Quit Event!")
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Gamelogic.move(board, 'w')
            elif event.key == pygame.K_a:
                Gamelogic.move(board, 'a')
            elif event.key == pygame.K_s:
                Gamelogic.move(board, 's')  
            elif event.key == pygame.K_d:
                Gamelogic.move(board, 'd')  

    if not run:
        break

    run = not Gamelogic.checkforwin(board)

    pygame.display.update()

pygame.quit()
