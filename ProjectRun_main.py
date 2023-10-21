from pico2d import *
import game_world
from player import Player

canvasSIZE = (1280, 720)
def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
             player.handle_event(event)

def create_world():
    global running
    global player

    running = True
    player = Player()
    game_world.add_object(player)

def update_world():
    game_world.updata()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas(canvasSIZE[0], canvasSIZE[1])
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)
# finalization code
close_canvas()