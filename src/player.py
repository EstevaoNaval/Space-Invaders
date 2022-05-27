from importlib.resources import path
from PPlay.sprite import *
from settings import *

path_nave = "./asset/nave/nave.png"
nave = Sprite(path_nave, 1)
nave.set_position((WIDTH - nave.width)/2, (HEIGHT - nave.height))