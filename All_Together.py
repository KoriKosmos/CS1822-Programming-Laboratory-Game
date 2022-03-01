try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import Vector
import math   
import random

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

#keyboard handler
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True
        elif key == simplegui.KEY_MAP['up']:
            self.up = True
        elif key == simplegui.KEY_MAP['down']:
            self.down = True
        elif key == simplegui.KEY_MAP['w']:
            self.w = True
        elif key == simplegui.KEY_MAP['a']:
            self.a = True
        elif key == simplegui.KEY_MAP['s']:
            self.s = True
        elif key == simplegui.KEY_MAP['d']:
            self.d = True
    
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
        elif key == simplegui.KEY_MAP['up']:
            self.up = False
        elif key == simplegui.KEY_MAP['down']:
            self.down = False
        elif key == simplegui.KEY_MAP['w']:
            self.w = False
        elif key == simplegui.KEY_MAP['a']:
            self.a = False
        elif key == simplegui.KEY_MAP['s']:
            self.s = False
        elif key == simplegui.KEY_MAP['d']:
            self.d = False

class Moving_Character:
    def __init__(self, pos, vel, spritesheet, direction_facing):
        self.pos = pos
        self.vel = vel
        self.spritesheet = spritesheet
        self.direction_facing = direction_facing

    def draw(self, canvas):
        #spritesheet.draw()
        canvas.draw_circle((self.pos.x, self.pos.y), 20, 1, "Green", "Green")

    def update_pos(self):
        self.pos += self.vel
        self.vel *= 0.8

class Player:
    def __init__(self, moving_character, bullet, health, damage, speed, width, height):
        self.moving_character = moving_character
        self.health = health
        self.damage = damage
        self.speed = speed
        self.width = width
        self.height = height

    def draw(self, canvas):
        self.moving_character.draw(canvas)
    
    def update_pos(self):

        #check not out of bounds
        if(self.moving_character.pos.x > CANVAS_WIDTH): #stuck on right wall
            if self.moving_character.vel.x > 0:
                self.moving_character.vel.x = 0
        elif(self.moving_character.pos.x < 0):  #stuck on left wall
            if self.moving_character.vel.x < 0:
                self.moving_character.vel.x = 0
        
        if(self.moving_character.pos.y > CANVAS_HEIGHT): #stuck on bottom
            if self.moving_character.vel.y > 0:
                self.moving_character.vel.y = 0
        elif(self.moving_character.pos.y < 0):  #stuck on top
            if self.moving_character.vel.y < 0:
                self.moving_character.vel.y = 0


        #move player pos
        self.moving_character.update_pos()
    
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
        #give player vel based on wasd
        if self.keyboard.w:
            self.player.moving_character.vel += Vector.Vector(0,-1)
        if self.keyboard.a:
            self.player.moving_character.vel += Vector.Vector(-1,0)
        if self.keyboard.s:
            self.player.moving_character.vel += Vector.Vector(0,1)
        if self.keyboard.d:
            self.player.moving_character.vel += Vector.Vector(1,0)
        self.player.update_pos()
    
#initialisation
keyboard = Keyboard()
player_char = Moving_Character(Vector.Vector(100,100), Vector.Vector(0,0), "", "")
player = Player(player_char, "", 5, 5, 5)
interaction = Interaction(player, keyboard)

#create frame
frame = simplegui.create_frame("Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_canvas_background('#004D26') #set background color

#keyboard handler
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)

frame.start()