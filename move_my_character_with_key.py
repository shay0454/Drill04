import os
from pico2d import *
os.chdir("C:\\github\\2Dprogramming\\Drill04")
TUK_WIDTH,TUK_HEIGHT=1280,1024
ch_size=[32,32]
running =True
dir=[0,0]
frame=0
def handle_event():
    global running,dir,frame
    events=get_events()
    for event in events:
        if event==SDL_KEYDOWN:
            if event==SDLK_LEFT:
                dir[0]-=1
            elif event==SDLK_RIGHT:
                dir[0]+=1
            elif event==SDLK_UP:
                dir[1]+=1
            elif event==SDLK_DOWN:
                dir[1]-=1
            elif event==SDLK_ESCAPE:
                running=False
        elif event==SDL_KEYUP:
            if event==SDLK_LEFT:
                dir[0]+=1
            elif event==SDLK_RIGHT:
                dir[0]-=1
            elif event==SDLK_UP:
                dir[1]-=1
            elif event==SDLK_DOWN:
                dir[1]+=1


open_canvas(TUK_WIDTH,TUK_HEIGHT)
character=load_image("character_v2.png")
TUK_GROUND=load_image("TUK_GROUND.png")
while(running):
    pass

close_canvas()