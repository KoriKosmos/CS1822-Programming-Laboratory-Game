from user304_rsf8mD0BOQ_1 import Vector
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
# Some constants
CANVAS_DIMS = (600, 400)

IMG = simplegui.load_image('https://cdn.discordapp.com/attachments/889956680480206888/948197429101080616/Hero_Vertical.png')
IMG_WIDTH = IMG.get_width()
print(IMG_WIDTH)
IMG_HEIGHT = IMG.get_height()
IMG_CENTRE = (IMG_WIDTH/2, IMG_HEIGHT/2)
IMG_DIMS = (IMG_WIDTH, IMG_HEIGHT)

STEP = 0.5

# Global variables
img_dest_dim = (128,128)
img_pos = [CANVAS_DIMS[0]/2, 2*CANVAS_DIMS[1]/3.]
img_rot = 0

WIDTH = 500
HEIGHT = 500

class Spritesheet:
    def __init__(self, imgURL, rows, columns, num_frames):
        self.img = simplegui.load_image(imgURL)
        sheetWIDTH = self.img.get_width()
        sheetHEIGHT = self.img.get_height()
        self.frameDimensions = (sheetWIDTH/columns, sheetHEIGHT/rows)
        self.clock = Clock()
        self.frameCenters = []
        self.currFrame = 0
        self.lastFrame = False
        
        for y in range(rows):
            for x in range(columns):
                temp_x = (sheetWIDTH/columns) * x
                temp_y = (sheetHEIGHT/rows) * y
                if (len(self.frameCenters) < num_frames):
                    self.frameCenters.append((temp_x + (sheetWIDTH/columns/2), temp_y + (sheetHEIGHT/rows/2)))
                
    def draw(self, canvas, pos, direction, vel, moving):
        self.clock.tick()
        print(moving)
        canvas.draw_image(self.img, self.frameCenters[self.currFrame], self.frameDimensions, pos, (64,64))
        if moving:
            if self.clock.transition(30):
                self.next_frame(direction)
        
    def next_frame(self, direction):
        if direction == 'down':
            if self.currFrame == 0:
                self.currFrame = 1
            elif self.currFrame == 1:
                self.currFrame = 0
            else:
                self.currFrame = 0
        if direction == 'up':
            if self.currFrame == 2:
                self.currFrame = 3
            elif self.currFrame == 3:
                self.currFrame = 2
            else:
                self.currFrame = 2
        if direction == 'left':
            if self.currFrame == 4:
                self.currFrame = 5
            elif self.currFrame == 5:
                self.currFrame = 4
            else:
                self.currFrame = 4
        if direction == 'right':
            if self.currFrame == 6:
                self.currFrame = 7
            elif self.currFrame == 7:
                self.currFrame = 6
            else:
                self.currFrame = 6
            
                
class Player:
    def __init__(self, pos, radius=10):
        self.pos = Vector(WIDTH/2,HEIGHT/2)
        self.vel = Vector()
        self.radius = max(radius,10)
        self.rot = 0
        self.direction = 'right'
        self.moving = False
        spritesheetImage = 'https://cdn.discordapp.com/attachments/889956680480206888/948197429101080616/Hero_Vertical.png'
        self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
        

    def draw(self, canvas):
        self.spritesheet.draw(canvas, self.pos.get_p(), self.direction, self.vel, self.moving)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        if self.pos.x < self.radius:
            self.pos.x = self.radius
        if self.pos.x > WIDTH - self.radius:
            self.pos.x = WIDTH - self.radius
        if self.pos.y < self.radius:
            self.pos.y = self.radius
        if self.pos.y > HEIGHT - self.radius:
            self.pos.y = HEIGHT - self.radius
            
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.moving = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if self.right or self.left or self.up or self.down:
            self.moving = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if not(self.right and self.left and self.up and self.down):
            self.moving = False
        if self.right or self.left or self.up or self.down:
            self.moving = True

class Clock:
    def __init__(self):
        self.time = 0
        
    def tick(self):
        self.time += 1
        
    def transition(self, frameDuration):
        return (self.time % frameDuration == 0)


class Interaction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.player.direction = 'right'
            self.player.vel.add(Vector(0.5, 0))
        if self.keyboard.left:
            self.player.direction = 'left'
            self.player.vel.add(Vector(-0.5, 0))
        if self.keyboard.up:
            self.player.direction = 'up'
            self.player.vel.add(Vector(0,-0.5))
        if self.keyboard.down:
            self.player.direction = 'down'
            self.player.vel.add(Vector(0,0.5))
        self.player.moving = self.keyboard.moving

kbd = Keyboard()
player = Player(Vector(WIDTH/2, HEIGHT-40), 40)
inter = Interaction(player, kbd)

def draw(canvas):
    inter.update()
    player.update()
    player.draw(canvas)

frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_canvas_background('White')
frame.start()
