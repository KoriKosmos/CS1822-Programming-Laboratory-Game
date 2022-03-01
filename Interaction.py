try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#import local class files
import random
import Keyboard
import Moving_Character
import Player
import Vector


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

    
class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard

    def draw(self, canvas):
        self.update() #update positions
        self.player.draw(canvas)
        #draw enemies
        #draw bullets

    def update(self):
        if self.keyboard.left:
            self.player.vel += Vector.Vector(0,1)
        self.player.update_pos()
    
#initialisation
keyboard = Keyboard()
player_char = Moving_Character.Moving_Character(Vector.Vector(100,100), Vector.Vector(0,0), "", "")
player = Player.Player(player_char, "", 5, 5, 5)
interaction = Interaction(player, keyboard)

#create frame
frame = simplegui.create_frame("Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_canvas_background('#004D26') #set background color

#keyboard handler
frame.set_keydown_handler(Keyboard.Keyboard.keyDown)
frame.set_keyup_handler(Keyboard.Keyboard.keyUp)

frame.start()
