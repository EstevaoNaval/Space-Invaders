import imp
import sys
import pygame
from pygame.locals import *
from settings import *
from menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.running, self.playing = 1, 0
        self.clock = pygame.time.Clock()

        self.bg_image = pygame.image.load("./asset/background/bg_image.png")
        self.display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.curr_menu = MainMenu(self)

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running, self.playing = 0, 0
                    self.curr_menu.run_display = 0

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RETURN: START_KEY = 1

                    if event.type == pygame.K_BACKSPACE: BACK_KEY = 1

                    if event.type == pygame.K_DOWN: DOWN_KEY = 1

                    if event.type == pygame.K_UP: UP_KEY = 1

    def reset_keys(self):
        UP_KEY, DOWN_KEY, START_KEY, BACK_KEY = 0, 0, 0, 0

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(FONT_PATH, size)
        text_surface = font.render(text, 1, BLACK)
        
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)

        self.window.blit(text_surface,text_rect)

    def game_loop(self):
        while self.running:
            self.clock.tick(FPS)
            self.check_events()

            if START_KEY: self.playing = 0
            self.display.fill(BLACK)

            self.window.blit(self.bg_image, (0,0))
            self.draw_text(TITLE, TITLE_FONT_SIZE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            pygame.display.update()
            self.reset_keys()
