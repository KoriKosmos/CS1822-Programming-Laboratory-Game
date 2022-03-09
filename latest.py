try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from user304_rsf8mD0BOQ_1 import Vector
#import Vector
import math   
import random

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

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

    def draw(self, canvas, pos, direction, moving):
        self.clock.tick()
        canvas.draw_image(self.img, self.frameCenters[self.currFrame], self.frameDimensions, (pos.x,pos.y), (64,64))
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

class Clock:
    def __init__(self):
        self.time = 0
        
    def tick(self):
        self.time += 1
        
    def transition(self, Duration):
        return (self.time % Duration == 0)

class Bullet:
    def __init__(self, pos, vel, damage, spritesheetImage, radius):
        self.pos = pos
        self.vel = vel
        self.damage = damage
        self.width = radius
        self.height = radius
        #self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
    
    def update_pos(self):
        self.pos += self.vel
    
    def draw(self, canvas):
        canvas.draw_circle((self.pos.x, self.pos.y), self.width, 1, "blue", "blue")
        
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
        
        self.moving = False #is player moving
        self.attacking = False #is player attacking
        
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
        
        if (self.w or self.a or self.s or self.d):
            self.moving = True
    
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
        
        if not(self.w or self.a or self.s or self.d):
            self.moving = False

class Enemy:
    def __init__(self, pos, vel, direction, health, speed, width, height, spritesheetImage):
        self.pos = pos
        self.pos = pos
        self.vel = vel
        self.direction = direction
        self.health = health
        self.width = width
        self.height = height
        self.speed = speed/10
        self.chase = False
        
        
        self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
        self.moving = False
        
        self.direction_list = ["left", "right", "up", "down", "stop"]
        
    def update_pos(self, player):
        #decide if enemy should change direction
        if(random.randint(1,50) == 50):
            self.direction = self.direction_list[random.randint(0,4)]
            
        self.chase_check(player)
        
        #move enemy vel
        if self.chase:
            if self.pos.y > player.pos.y:
                self.vel += Vector(0, -self.speed)
                self.moving = True
                self.direction = 'up'
            if self.pos.y < player.pos.y:
                self.vel += Vector(0, self.speed)
                self.moving = True
                self.direction = 'down'
            if self.pos.x > player.pos.x:
                self.vel += Vector(-self.speed, 0)
                self.moving = True
                self.direction = 'left'
            if self.pos.x < player.pos.x:
                self.vel += Vector(self.speed, 0)
                self.moving = True
                self.direction = 'right'
        else:
            if self.direction == "left":
                self.vel += Vector(-self.speed, 0)
                self.moving = True
            elif self.direction == "right":
                self.vel += Vector(self.speed, 0)
                self.moving = True
            elif self.direction == "up":
                self.vel += Vector(0, -self.speed)
                self.moving = True
            elif self.direction == "down":
                self.vel += Vector(0, self.speed)
                self.moving = True
            elif self.direction == "stop":	#enemy is stopped
                self.vel = Vector(0, 0)
                self.moving = False
            
        #check not out of bounds
        if(self.pos.x > CANVAS_WIDTH - self.width): #stuck on right wall
            if self.vel.x > 0:
                self.vel.x = 0
                self.direction = "left"
        elif(self.pos.x < 0 + self.width):  #stuck on left wall
            if self.vel.x < 0:
                self.vel.x = 0
                self.direction = "right"
        if(self.pos.y > CANVAS_HEIGHT - self.height): #stuck on bottom
            if self.vel.y > 0:
                self.vel.y = 0
                self.direction = "up"
        elif(self.pos.y < 0 + self.height):  #stuck on top
            if self.vel.y < 0:
                self.vel.y = 0
                self.direction = "down"
            
        #move enemy pos
        self.pos += self.vel
        self.vel *= 0.8
        
    def draw(self, canvas):
        self.spritesheet.draw(canvas, self.pos, self.direction, self.moving)
    
    def chase_check(self, object):
        range = 200
        xOverlap = (((self.pos.x - self.width) - range) < ((object.pos.x + object.width) + range)) and (((self.pos.x + self.width) + range) > ((object.pos.x - object.width) - range))
        yOverlap = (((self.pos.y - self.height) - range) < ((object.pos.y + object.height) + range)) and (((self.pos.y + self.height) + range) > ((object.pos.y - object.height) - range))
        if (xOverlap and yOverlap):
            self.chase = True
    
class Player:
    def __init__(self, pos, vel, direction, health, damage, speed, width, height):
        self.pos = pos
        self.vel = vel
        self.direction = direction
        self.speed = speed/10
        self.health = health
        self.damage = damage

        self.width = width
        self.height = height
        
        self.moving = False
        spritesheetImage = 'https://cdn.discordapp.com/attachments/889956680480206888/948197429101080616/Hero_Vertical.png'
        self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
    
        self.can_shoot = False #can player shoot
        self.clock = Clock()
        
    def update_pos(self):
        #check not out of bounds
        if(self.pos.x > CANVAS_WIDTH - self.width): #stuck on right wall
            if self.vel.x > 0:
                self.vel.x = 0
        elif(self.pos.x < 0 + self.width):  #stuck on left wall
            if self.vel.x < 0:
                self.vel.x = 0
        
        if(self.pos.y > CANVAS_HEIGHT - self.height): #stuck on bottom
            if self.vel.y > 0:
                self.vel.y = 0
        elif(self.pos.y < 0 + self.height):  #stuck on top
            if self.vel.y < 0:
                self.vel.y = 0

        #move player pos
        self.pos += self.vel
        self.vel *= 0.8
        
        if not self.can_shoot:
            self.clock.tick()
            if(self.clock.transition(50)):
                self.can_shoot = True
        
    def draw(self, canvas):
        self.spritesheet.draw(canvas, self.pos, self.direction, self.moving)

        
class Interaction:
    def __init__(self, player, keyboard, enemy_list):
        self.player = player
        self.keyboard = keyboard
        self.enemy_list = enemy_list
        global player_bullet
        global enemy_bullet
        
    def draw(self, canvas):
        self.update() #update positions
        #draw bullets
        for i in player_bullet:
            i.draw(canvas)

        #draw enemies
        for i in enemy_list:
            i.draw(canvas)
        
        self.player.draw(canvas)#draw player
        
    def update(self):
        #check if player is dead
        if self.player.health <= 0:
            print("Game Over")
            quit()
        
        #give player vel based on wasd
        if self.keyboard.w:
            self.player.direction = "up"	#player moving up
            self.player.vel += Vector(0,-self.player.speed)
        if self.keyboard.a:
            self.player.direction = "left"
            self.player.vel += Vector(-self.player.speed,0)
        if self.keyboard.s:
            self.player.direction = "down"
            self.player.vel += Vector(0,self.player.speed)
        if self.keyboard.d:
            self.player.direction = "right"
            self.player.vel += Vector(self.player.speed,0)
        self.player.moving = self.keyboard.moving #is player moving or not
       
        if self.player.can_shoot:
            if self.keyboard.left:	#player is shooting left
                player_bullet.append(Bullet(self.player.pos, self.player.vel/3 + Vector(-4, 0), self.player.damage, "", 5))
                self.player.direction = "left"
                self.player.can_shoot = False
            elif self.keyboard.right:	#player is shooting right
                player_bullet.append(Bullet(self.player.pos, self.player.vel/3 + Vector(4, 0), self.player.damage, "", 5))
                self.player.direction = "right"
                self.player.can_shoot = False
            elif self.keyboard.up:	#player is shooting up
                player_bullet.append(Bullet(self.player.pos, self.player.vel/3 + Vector(0, -4), self.player.damage, "", 5))
                self.player.direction = "up"
                self.player.can_shoot = False
            elif self.keyboard.down:	#player is shooting down
                player_bullet.append(Bullet(self.player.pos, self.player.vel/3 + Vector(0, 4), self.player.damage, "", 5))
                self.player.direction = "down"
                self.player.can_shoot = False
            
        for i in self.enemy_list:	#update enemy positions
            i.update_pos(player)
        for i in player_bullet:	#update bullet positions
            i.update_pos()
            
        self.player.update_pos() #update player position
        self.check_collisions() #check if bullets have hit enemy/player

        
    def check_collisions(self):
        remove_enemy = []
        remove_bullet = []
        for bullet in player_bullet:	#check if player bullet has hit enemy
            for enemy in self.enemy_list:
                if self.collision(bullet, enemy):
                    enemy.health -= bullet.damage #damage enemy
                    if enemy.health <= 0:	#check if enemy is dead
                        remove_enemy.append(enemy)
                    remove_bullet.append(bullet)
        
        #check if enemy hits player
        for enemy in self.enemy_list:
            if self.collision(self.player, enemy):
                remove_enemy.append(enemy)
                self.player.health -= 50
            
        #clean up bullets and enemies
        for item in remove_enemy:
            self.enemy_list.remove(item)
        for item in remove_bullet:
            player_bullet.remove(item)
    
    def collision(self, object1, object2):
        xOverlap = (((object1.pos.x - object1.width) < (object2.pos.x + object2.width)) and ((object1.pos.x + object1.width) > (object2.pos.x - object2.width)))
        yOverlap = (((object1.pos.y - object1.height) < (object2.pos.y + object2.height)) and ((object1.pos.y + object1.height) > (object2.pos.y - object2.height)))
        return xOverlap and yOverlap
    
      
    
#INITIALISATION
player_bullet = []
enemy_bullet = []
enemy_list = []
#add enemy to enemy list
enemy_url = "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Flame_Oni.png"
enemy_list.append(Enemy(Vector(1000, 500), Vector(0,0), "stop", 100, 4, 30, 50, enemy_url))
enemy_list.append(Enemy(Vector(1000, 200), Vector(0,0), "stop", 100, 4, 30, 50, enemy_url))
enemy_list.append(Enemy(Vector(1000, 400), Vector(0,0), "stop", 100, 4, 60, 50, enemy_url))
enemy_list.append(Enemy(Vector(1000, 300), Vector(0,0), "stop", 100, 4, 30, 50, enemy_url))

keyboard = Keyboard()
player = Player(Vector(100, 100), Vector(0, 0), "right", 150, 50, 5, 30, 30)
interaction = Interaction(player, keyboard, enemy_list)


#create frame
frame = simplegui.create_frame("Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_canvas_background('#004D26') #set background color

#keyboard handler
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)

frame.start()
