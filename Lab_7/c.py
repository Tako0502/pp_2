import pygame
import os

def list_files(path):
    files = []
    items = os.listdir(path)
    
    for item in items:
        item_path = path + '/' + item
        
        if os.path.isdir(item_path):
            continue
        else:
            files.append(item_path)
    
    return files

def get_file_name(file_path):
    base_name = os.path.basename(file_path)  
    file_name, _ = os.path.splitext(base_name) 
    return file_name
directory = "/Users/talanterzhan/Desktop/Musics"
music_list = list_files(directory)
pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Music Player")

current_music_index = 0
pygame.mixer.music.load(music_list[current_music_index])

button_width, button_height = 200, 100
button_x, button_y = (win_width - button_width) // 2, (win_height - button_height) // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
play_icon = pygame.transform.scale(pygame.image.load("play.png"), (button_width - 20, button_height - 20))
pause_icon = pygame.transform.scale(pygame.image.load("pause.webp"), (button_width - 20, button_height - 20))
previous_icon = pygame.transform.scale(pygame.image.load("prev.png"), (button_width - 20, button_height - 20))
next_icon = pygame.transform.scale(pygame.image.load("next.png"), (button_width - 20, button_height - 20))

playing = False

def draw_button():
    button_x, button_y = (win_width - button_width) // 2, (win_height - button_height) // 2
    pygame.draw.rect(win, WHITE, (button_x, button_y - 150, button_width, button_height))
    pygame.draw.rect(win, WHITE, (button_x - 200, button_y, button_width, button_height))
    pygame.draw.rect(win, WHITE, (button_x + 200, button_y, button_width, button_height))

    if playing:
        win.blit(pause_icon, (button_x + button_width / 2 - pause_icon.get_width() / 2,
                              button_y - 150 + button_height / 2 - pause_icon.get_height() / 2))
    else:
        win.blit(play_icon, (button_x + button_width / 2 - play_icon.get_width() / 2,
                             button_y - 150 + button_height / 2 - play_icon.get_height() / 2))
    win.blit(previous_icon, (button_x - 200 + button_width / 2 - previous_icon.get_width() / 2,
                             button_y + button_height / 2 - previous_icon.get_height() / 2))
    win.blit(next_icon, (button_x + 200 + button_width / 2 - next_icon.get_width() / 2,
                         button_y + button_height / 2 - next_icon.get_height() / 2))

def draw_music_name():
    font = pygame.font.Font(None, 36)
    text = font.render(get_file_name(music_list[current_music_index]), True, WHITE)
    text_rect = text.get_rect(center=(win_width // 2, win_height - 50))
    win.blit(text, text_rect)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_x, button_y = (win_width - button_width) // 2, (win_height - button_height) // 2
            if button_x <= mouse_pos[0] <= button_x + button_width and \
                    button_y - 150 <= mouse_pos[1] <= button_y - 150 + button_height:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif button_x - 200 <= mouse_pos[0] <= button_x - 200 + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
                current_music_index = (current_music_index - 1) % len(music_list)
                pygame.mixer.music.load(music_list[current_music_index])
                if playing:
                    pygame.mixer.music.play()
            elif button_x + 200 <= mouse_pos[0] <= button_x + 200 + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
                current_music_index = (current_music_index + 1) % len(music_list)
                pygame.mixer.music.load(music_list[current_music_index])
                if playing:
                    pygame.mixer.music.play()
    win.fill(BLACK)
    draw_button()
    draw_music_name()
    pygame.display.update()

pygame.quit()
