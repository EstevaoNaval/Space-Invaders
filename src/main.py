from PPlay.gameimage import GameImage
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from PPlay.sprite import *
from settings import *
from pygame import time
import sys

#def move_nave(keycode, nave):
#    if(keycode.key_pressed["LEFT"]):
#        nave.move_key_x(4)

def draw(nave, matrix_invader, bullets):
    nave.draw()

    for row in range(len(matrix_invader)):
        for column in range(len(matrix_invader[row])):
            matrix_invader[row][column].draw()

    for bullet in bullets:
        bullet.draw()

def draw_fps(fps, list_position, size, color, font_name, janela):
    int_fps_2_string = str(int(fps))
    janela.draw_text("FPS: " + int_fps_2_string, list_position[0], list_position[1], size, color, font_name)


def move_bullets(bullets, janela):
    nave_bullet_direction = -1
    
    for row in range(len(bullets)):
        bullets[row].move_y(BULLET_SPEED * janela.delta_time() * GAME_SPEED * nave_bullet_direction)

        if bullets[row].y < -bullets[row].height or bullets[row].y > janela.height + bullets[row].height:
            del bullets[row]
            return bullets

    return bullets

def set_bullet_position(bullet, atirador):
    shoot_x = atirador.x + (atirador.width/2) - (bullet.width/2)
    shoot_y = atirador.y + atirador.height - bullet.height

    bullet.x = shoot_x
    bullet.y = shoot_y

def set_nave(path_nave):
    nave = Sprite(path_nave, 1)
    nave.set_position((WIDTH - nave.width)/2, (HEIGHT - nave.height))

    return nave

def set_invander(path_invader, row, column):
    invader = Sprite(path_invader, 1)
    x, y = (column * invader.width) + 270, row * invader.height
    invader.set_position(x, y)
    
    return invader

def move_invader(matrix_invaders, janela, tempoDescida, invader_direction):
    if tempoDescida > 0.15:
        if(matrix_invaders[0][0].x <= 0 or matrix_invaders[0][-1].x + matrix_invaders[0][-1].width >= janela.width):
            invader_direction[0] *= -1
            for row in range(len(matrix_invaders)):
                for column in range(len(matrix_invaders[row])):
                    matrix_invaders[row][column].move_y(750 * GAME_SPEED * janela.delta_time())
            tempoDescida = 0
    else: tempoDescida += janela.delta_time()

    for row in range(len(matrix_invaders)):
        for column in range(len(matrix_invaders[row])):
            matrix_invaders[row][column].move_x(INVADER_SPEED * janela.delta_time() * GAME_SPEED * invader_direction[0])

    return tempoDescida

def set_matrix_invader(path_invader, num_row_invader, num_column_invader):
    matrix_invaders = []
    for i in range(num_row_invader): matrix_invaders.append([0] * num_column_invader)

    for row in range(num_row_invader):
        for column in range(num_column_invader):
            matrix_invaders[row][column] = set_invander(path_invader, row, column)
    
    return matrix_invaders

def shoot(atirador, path_bullet):
    shoot_tick = 0

    bullet = Sprite(path_bullet)

    set_bullet_position(bullet, atirador)

    bullets.append(bullet)

    return shoot_tick

def handle_nave_collision(nave):
    if nave.x < 0: nave.x = 0
    elif nave.x + nave.width > WIDTH: nave.x = WIDTH - nave.width

def handle_bullet_collision(bullets, invaders):
    for index_bullet in range(len(bullets)):
        if (bullets[index_bullet].y <= invaders[-1][0].y + invaders[-1][0].height) and (bullets[index_bullet].y >= invaders[0][0].y):
            for index_bullet in range(0, len(bullets)):
                for row in range(len(invaders) - 1, -1, -1):
                    for column in range(len(invaders[row])):
                        if bullets[index_bullet].collided(invaders[row][column]):
                            del(bullets[index_bullet])
                            del(invaders[row][column])

                            if not invaders[row]: del invaders[row]

                            return bullets, invaders
    
    return bullets, invaders

janela = Window(WIDTH, HEIGHT)
janela.set_title(TITLE)

clock = time.Clock()

path_bg = "./assets/background/bg.png"
fundo = GameImage(path_bg)

key = Keyboard()

nave = set_nave("./assets/nave/nave.png")
direcao_nave = 1

path_bullet = "./assets/bullet/pixel_laser_black.png"
bullets = []

path_invader = "./assets/invader/invader_01.png"
matrix_invaders = set_matrix_invader(path_invader, NUM_ROW_INVADER, NUM_COLUMN_INVADER)
invader_direction_x = [1]

enemy_shoot_delay = 1/GAME_SPEED 
shoot_delay = 1/GAME_SPEED * 0.5
shoot_tick = shoot_delay
tempoDescida = 0

running = 1

min_FPS = 2000

while running:
    clock.tick()
    
    janela.set_background_color(DARKGREY)
    fundo.draw()

    shoot_tick += janela.delta_time()

    handle_nave_collision(nave)

    if(key.key_pressed("LEFT")): nave.move_x(-NAVE_SPEED * janela.delta_time())
    elif(key.key_pressed("RIGHT")): nave.move_x(NAVE_SPEED * janela.delta_time())
    if(key.key_pressed("SPACE")): 
        if shoot_tick > shoot_delay:
            # Chama a função shoot(), para que ela efetue do disparo
            shoot_tick = shoot(nave, path_bullet)
    
    tempoDescida = move_invader(matrix_invaders, janela, tempoDescida, invader_direction_x)
    bullets = move_bullets(bullets, janela)

    bullets, matrix_invaders = handle_bullet_collision(bullets, matrix_invaders)

    draw(nave, matrix_invaders, bullets)
    draw_fps(clock.get_fps(), [0,0], 20, BLACK, FONT_NAME, janela)
    
    janela.update()
