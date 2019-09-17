import pygame
from pygame.locals import *
import os
# from characters import *


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

#Static objects
background_map_original = pygame.image.load('assets/default_map_960x600.jpeg').convert_alpha()
background_map = pygame.transform.scale(background_map_original, (screen_width, screen_height)).convert_alpha()
map_rect = background_map.get_rect()
tile = pygame.image.load('assets/tile.png').convert_alpha()
tile = pygame.transform.scale(tile, (80, 80)).convert_alpha()

# Static Locations
tile_locations = {
	'A1': (0, 0),
	'A2': (0, 0),
	'A3': (0, 0),
	'A4': (0, 0),
	'A5': (0, 0),
	'A6': (0, 0),
	'A7': (0, 0),
	'B1': (0, 0),
	'B2': (0, 0),
	'B3': (0, 0),
	'B4': (0, 0),
	'B5': (0, 0),
	'B6': (0, 0),
	'B7': (0, 0),
	'C1': (273, 455),
	'C2': (0, 0),
	'C3': (0, 0),
	'C4': (0, 0),
	'C5': (0, 0),
	'C6': (0, 0),
	'C7': (0, 0),
}
# Get characters
# characters_lst = characters.get_characters()


# Game Framerate
clock = pygame.time.Clock()
FPS = 30
# Main Menu
def main_menu():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			screen.blit(background_map, (screen_width/2 - map_rect[2]/2, 0))
			screen.blit(tile, tile_locations['C1'])

		# Update
		pygame.display.update()
		clock.tick(FPS)

def find_path()

# Main Game Loop
crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	main_menu()
	pygame.quit()
	quit()