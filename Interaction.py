import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import Vector
import Keyboard

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

    
class Interaction:
    def __init__(self):
        pass
    
    def draw(self, canvas):
        pass

#initialisation
Keyboard = Keyboard.Keyboard()
interaction = Interaction()


#create frame
frame = simplegui.create_frame("Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_canvas_background('#004D26') #set background color

#keyboard handler
frame.set_keydown_handler(Keyboard.keyDown)
frame.set_keyup_handler(Keyboard.keyUp)

frame.start()