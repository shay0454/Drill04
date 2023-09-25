import os
from pico2d import *
os.chdir("C:\\github\\2Dprogramming\\Drill04")
TUK_WIDTH,TUK_HEIGHT=1280,1024
ch_size=[32,32]
running =True
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
dir=[0,0]
frame=0
see_direction=''
def handle_event():
    global running,dir,frame,see_direction
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_LEFT:
                dir[0]-=1
                see_direction='h'
            elif event.key==SDLK_RIGHT:
                dir[0]+=1
                see_direction=''
            elif event.key==SDLK_UP:
                dir[1]+=1
            elif event.key==SDLK_DOWN:
                dir[1]-=1
            elif event.key==SDLK_ESCAPE:
                running=False
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_LEFT:
                dir[0]+=1
            elif event.key==SDLK_RIGHT:
                dir[0]-=1
            elif event.key==SDLK_UP:
                dir[1]-=1
            elif event.key==SDLK_DOWN:
                dir[1]+=1
    frame=(frame+1)%8


open_canvas(TUK_WIDTH,TUK_HEIGHT)
ch=load_image("character_v2.png")
TUK_GROUND=load_image("TUK_GROUND.png")
while(running):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    ch.clip_composite_draw(frame*32,32*6,ch_size[0],ch_size[1],0,see_direction,x,y,128,128)
    update_canvas()
    handle_event()
    x+=dir[0]*10
    y+=dir[1]*10
    delay(0.03)

close_canvas()