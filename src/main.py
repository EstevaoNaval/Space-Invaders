from PPlay.gameimage import GameImage
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.keyboard import *
from PPlay.sprite import *
from settings import *

#def move_nave(keycode, nave):
#    if(keycode.key_pressed["LEFT"]):
#        nave.move_key_x(4)

def draw(nave, bullets):
    nave.draw()

    for bullet in bullets:
        bullet.draw()

def move_bullets(bullets, janela):
    nave_bullet_direction = -1
    
    for bullet in bullets:
        bullet.move_y(BULLET_SPEED * janela.delta_time() * GAME_SPEED * nave_bullet_direction)

        if bullet.y < -bullet.height or bullet.y > janela.height + bullet.height:
            bullets.remove(bullet)

def set_bullet_position(bullet, atirador):
    shoot_x = atirador.x + (atirador.width/2) - (bullet.width/2)
    shoot_y = atirador.y + atirador.height - bullet.height

    bullet.x = shoot_x
    bullet.y = shoot_y


def shoot(atirador, path_bullet):
    shoot_tick = 0

    bullet = Sprite(path_bullet)

    set_bullet_position(bullet, atirador)

    bullets.append(bullet)

    return shoot_tick

def handle_nave_collision(nave, janela):
    if nave.x < 0: nave.x = 0
    elif nave.x + nave.width > WIDTH: nave.x = WIDTH - nave.width

janela = Window(WIDTH, HEIGHT)
janela.set_title(TITLE)

path_bg = "./assets/background/bg.png"
fundo = GameImage(path_bg)

key = Keyboard()

path_nave = "./assets/nave/nave.png"
nave = Sprite(path_nave, 1)
nave.set_position((WIDTH - nave.width)/2, (HEIGHT - nave.height))

path_bullet = "./assets/bullet/pixel_laser_black.png"
bullets = []

enemy_shoot_delay = 1/GAME_SPEED 
shoot_delay = 1/GAME_SPEED * 0.5
shoot_tick = shoot_delay

running = 1

while running:
    janela.set_background_color(DARKGREY)
    
    fundo.draw()

    shoot_tick += janela.delta_time()

    handle_nave_collision(nave, janela)

    if(key.key_pressed("LEFT")): nave.move_x(-NAVE_SPEED * janela.delta_time())
    elif(key.key_pressed("RIGHT")): nave.move_x(NAVE_SPEED * janela.delta_time())
    if(key.key_pressed("SPACE")): 
        if shoot_tick > shoot_delay:
            # Chama a função shoot(), para que ela efetue do disparo
            shoot_tick = shoot(nave, path_bullet)
    
    move_bullets(bullets, janela)

    draw(nave, bullets)

    janela.update()
