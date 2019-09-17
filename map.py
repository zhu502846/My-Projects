import pygame
from pygame.locals import *
import os
from story import *
# Game Initialization
pygame.init()
pygame.display.set_caption("Game")

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width = 1280
screen_height = 800

screen=pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
 
# Game Fonts
menu_font = "fonts/mohave-italic.otf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30
# Main Menu
def main_menu():

	#Static Objects
	screen.fill(blue)
	title = text_format("TITLE PLACEHOLDER", menu_font, 90, yellow)

	selected = 'new_game'
 
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if selected == 'new_game':
						selected = 'exit'
					elif selected == 'load_game':
						selected = 'new_game'
					elif selected == 'options':
						selected = 'load_game'
					else:
						selected = 'options'
				elif event.key == pygame.K_DOWN:
					if selected == 'new_game':
						selected = 'load_game'
					elif selected == 'load_game':
						selected = 'options'
					elif selected == 'options':
						selected = 'exit'
					else:
						selected = 'new_game'
				if event.key == pygame.K_x:
					if selected == "new_game":
						return selected
					if selected == 'load_game':
						return selected
					if selected == 'options':
						return selected
					if selected == 'exit':
						pygame.quit()
						quit()
				if event.key == pygame.K_z:
					selected = 'exit'
 
		# Main Menu UI
		if selected == "new_game":
			text_new_game = text_format("New Game", menu_font, 75, white)
		else:
			text_new_game = text_format("New Game", menu_font, 75, black)
		if selected == "load_game":
			text_load_game=text_format("Load Game", menu_font, 75, white)
		else:
			text_load_game = text_format("Load Game", menu_font, 75, black)
		if selected == "options":
			text_options = text_format("Options", menu_font, 75, white)
		else:
			text_options = text_format("Options", menu_font, 75, black)
		if selected == "exit":
			text_exit = text_format("Exit", menu_font, 75, white)
		else:
			text_exit = text_format("Exit", menu_font, 75, black)
		title_rect = title.get_rect()
		new_game_rect = text_new_game.get_rect()
		load_game_rect = text_load_game.get_rect()
		options_rect = text_options.get_rect()
		exit_rect = text_exit.get_rect()
 
		# Main Menu Text
		screen.blit(title, (screen_width/3 - (title_rect[2]/2), 45))
		screen.blit(text_new_game, (screen_width - (new_game_rect[2] + 15), 80))
		screen.blit(text_load_game, (screen_width - (load_game_rect[2] + 15), 150))
		screen.blit(text_options, (screen_width - (options_rect[2] + 15), 220))
		screen.blit(text_exit, (screen_width - (exit_rect[2] + 15), 290))

		# Update
		pygame.display.update()
		clock.tick(FPS)

def begin_game():
	return None

# Main Game Loop
crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	choice = main_menu()
	if choice == 'new_game':
		main()
	pygame.quit()
	quit()