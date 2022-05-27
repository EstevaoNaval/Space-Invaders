from PPlay.window import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from player import *
from settings import *

def move_nave(keycode, nave):
    if(keycode.key_pressed["LEFT"]):
        nave.move_key_x(4)

def draw(nave):
    nave.draw()


janela = Window(WIDTH, HEIGHT)
janela.set_title(TITLE)
janela.set_background_color(DARKGREY)

key = Keyboard()

running = 1

while running:
    draw(nave)
    if(key.key_pressed("LEFT")): nave.move_x(GAME_SPEED * janela.delta_time())

    janela.update()
