import os
from pico2d import *
os.chdir("C:\\github\\2Dprogramming\\Drill04")
TUK_WIDTH,TUK_HEIGHT=1280,1024
ch_size=[32,32]
running =True
x,y=0,0
frame=0
def handle_event():
    pass
open_canvas(TUK_WIDTH,TUK_HEIGHT)
character=load_image("character_v2.png")
TUK_GROUND=load_image("TUK_GROUND.png")


close_canvas()