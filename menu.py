import pygame
from pygame.locals import *
from settings import BLACK, DOWN_KEY, SCREEN_HEIGHT, SCREEN_WIDTH, START_KEY, TITLE, TITLE_FONT_SIZE, UP_KEY


class Menu:

    def __init__(self, game):
        self.game = game
        self.mid_width, self.mid_height = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        self.run_display = 1
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("X", 50, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        pygame.display.update()
        self.game.window.blit(self.game.bg_image, (0,0))
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game_state = 1
        self.start_x, self.start_y = self.mid_width, self.mid_width + 30
        self.difficult_x, self.difficult_y = self.mid_width, self.mid_height + 50
        self.ranking_x, self.ranking_y = self.mid_width, self.mid_height + 70
        self.exit_x, self.exit_y = self.mid_width, self.mid_height + 90
        self.cursor_rect_midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = 1
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text(TITLE, 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)
            self.game.draw_text("Jogar", 20, self.start_x, self.start_y)
            self.game.draw_text("Dificuldade", 20, self.difficult_x, self.difficult_y)
            self.game.draw_text("Ranking", 20, self.ranking_x, self.ranking_y)
            self.game.draw_text("Sair", 20, self.exit_x, self.exit_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if DOWN_KEY:
            if self.game_state == 1:
                self.cursor_rect.midtop = (self.difficult_x + self.offset, self.difficult_y)
                self.game_state = 2
            elif self.game_state == 2:
                self.cursor_rect.midtop = (self.ranking_x + self.offset, self.ranking_y)
                self.game_state = 3
            elif self.game_state == 3:
                self.cursor_rect.midtop = (self.exit_x + self.offset, self.exit_y)
                self.game_state = 4
            elif self.game_state == 4:
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.game_state = 1
        elif UP_KEY:
            if self.game_state == 1:
                self.cursor_rect.midtop = (self.exit_x + self.offset, self.exit_y)
                self.game_state = 4
            elif self.game_state == 2:
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.game_state = 1
            elif self.game_state == 3:
                self.cursor_rect.midtop = (self.difficult_x + self.offset, self.difficult_y)
                self.game_state = 2
            elif self.game_state == 4:
                self.cursor_rect.midtop = (self.ranking_x + self.offset, self.ranking_y)
                self.game_state = 3
    
    def check_input(self):
        self.move_cursor()
        if START_KEY:
            if self.game_state == 1:
                self.game.playing = 1
            elif self.game_state == 2:
                pass
            elif self.game_state == 3:
                pass
            self.run_display = 0