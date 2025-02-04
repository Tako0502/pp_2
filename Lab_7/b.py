import pygame
import sys

pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
icon = pygame.image

pygame.display.set_caption("My Pygame pp2")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
square_x = win_width // 2
square_y = win_height // 2
square_size = 100
square_speed_x = 0
square_speed_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                square_speed_x = 0
                square_speed_y = -5
            elif event.key == pygame.K_DOWN:
                square_speed_x = 0
                square_speed_y = 5
            elif event.key == pygame.K_LEFT:
                square_speed_x = -5
                square_speed_y = 0
            elif event.key == pygame.K_RIGHT:
                square_speed_x = 5
                square_speed_y = 0

    square_x += square_speed_x
    square_y += square_speed_y

    if square_x < -square_size:
        square_x = win_width
    elif square_x > win_width:
        square_x = -square_size
    if square_y < -square_size:
        square_y = win_height
    elif square_y > win_height:
        square_y = -square_size
    win.fill((255, 255, 255))
    pygame.draw.rect(win, BLUE, (square_x, square_y, square_size, square_size))
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
