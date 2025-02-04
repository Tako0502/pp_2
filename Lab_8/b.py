import pygame
import sys
import random
import time
from pygame.locals import *

black_colour = pygame.Color(28, 56, 20)
blue = pygame.Color(8, 96, 168)
red_colour = pygame.Color(230, 75, 8)
green_colour = pygame.Color(8, 168, 24)  
grey_colour = pygame.Color(150, 150, 150)
background_image = pygame.image.load("field.png")

def gameover(gamesurface, points):
    gameover_font = pygame.font.SysFont("MicrosoftYaHei", 50)
    game_over_sound = pygame.mixer.Sound('game-over.mp3')
    game_over_sound.play()
    gameover_colour = gameover_font.render('Game Over', True, grey_colour)
    gameover_location = gameover_colour.get_rect()
    gameover_location.midtop = (480, 300)
    gamesurface.blit(gameover_colour, gameover_location)

    points_font = pygame.font.SysFont("MicrosoftYaHei", 30)
    points_text = points_font.render('Points: ' + str(points), True, pygame.Color(255, 255, 255))
    points_rect = points_text.get_rect()
    points_rect.midtop = (480, 400)
    gamesurface.blit(points_text, points_rect)

    button_font = pygame.font.SysFont("MicrosoftYaHei", 35)
    button_text = button_font.render('Replay', True, pygame.Color(255, 255, 255))
    button_rect = button_text.get_rect()
    button_rect.center = (480, 500)
    pygame.draw.rect(gamesurface, red_colour, button_rect)
    gamesurface.blit(button_text, button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    main()

def main():
    pygame.init()
    pygame.time.Clock()
    ftpsClock = pygame.time.Clock()
    gamesurface = pygame.display.set_mode((960, 640))
    snakeposition = [480, 320]
    snakelength = [[100, 100], [80, 100], [60, 100]]
    square_purpose = [300, 300]
    square_position = 1
    derection = "down"
    change_derection = derection
    eaten_count = 0
    speed = 2
    last_eat_time = time.time()
    new_dish_delay = 5 
    food_color = red_colour  
    food_type = 'common'  
    dish_counter = 0  
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_derection = "right"
                if event.key == K_LEFT or event.key == ord('a'):
                    change_derection = "left"
                if event.key == K_UP or event.key == ord('w'):
                    change_derection = "up"
                if event.key == K_DOWN or event.key == ord('s'):
                    change_derection = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        if change_derection == 'left' and not derection == 'right':
            derection = change_derection
        if change_derection == 'right' and not derection == 'left':
            derection = change_derection
        if change_derection == 'up' and not derection == 'down':
            derection = change_derection
        if change_derection == 'down' and not derection == 'up':
            derection = change_derection
        if derection == 'left':
            snakeposition[0] -= 20
        if derection == 'right':
            snakeposition[0] += 20
        if derection == 'up':
            snakeposition[1] -= 20
        if derection == 'down':
            snakeposition[1] += 20
        snakelength.insert(0, list(snakeposition))
        
        if time.time() - last_eat_time > new_dish_delay:
            square_position = 0  
            last_eat_time = time.time()  

            dish_counter += 1
            if dish_counter % 3 == 0:
                food_type = 'green'
                food_color = green_colour
            else:
                food_type = 'common'
                food_color = red_colour
        
        if snakeposition[0] == square_purpose[0] and snakeposition[1] == square_purpose[1]:
            last_eat_time = time.time()  
            square_position = 0
            if food_type == 'common':
                eaten_count += 1
            elif food_type == 'green':
                eaten_count += 5
            if eaten_count % 3 == 0: 
                speed += 1
        else:
            snakelength.pop()
        if square_position == 0:
            x = random.randrange(1, 48)
            y = random.randrange(1, 32)
            square_purpose = [int(x * 20), int(y * 20)]
            square_position = 1
        scaled_background_image = pygame.transform.scale(background_image, (960, 640))
        gamesurface.blit(scaled_background_image, (0, 0))
        for position in snakelength:
            pygame.draw.rect(gamesurface, blue, Rect(position[0], position[1], 20, 20))
            if food_color:
                dish_counter+=1
                pygame.draw.rect(gamesurface, food_color, Rect(square_purpose[0], square_purpose[1], 20, 20))
        
        points_font = pygame.font.SysFont("MicrosoftYaHei", 30)
        points_text = points_font.render('Points: ' + str(eaten_count), True, pygame.Color(255, 255, 255))
        points_rect = points_text.get_rect()
        points_rect.topright = (940, 10)
        gamesurface.blit(points_text, points_rect)

        pygame.display.flip()
        if snakeposition[0] < 0 or snakeposition[0] > 940:
            gameover(gamesurface, eaten_count)
        if snakeposition[1] < 0 or snakeposition[1] > 620:
            gameover(gamesurface, eaten_count)
        for snakebody in snakelength[1:]:
            if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                gameover(gamesurface, eaten_count)
        ftpsClock.tick(speed*3)

if __name__ == "__main__":
    main()
