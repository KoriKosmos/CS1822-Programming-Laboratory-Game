try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from user304_rsf8mD0BOQ_1 import Vector
# import Vector
import math
import random

CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 720


class Maps:
    map_count = 0

    maps = ["https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/FourFloor.png",
            "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/FourFloorWhite.png",
            "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/FourFloorMellowYellow.png",
            "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/FourFloorGreen.png"]

    IMG = simplegui.load_image(maps[random.randint(0, 3)])
    SHEET_WIDTH = IMG.get_width()
    SHEET_HEIGHT = IMG.get_height()
    SHEET_COLUMNS = 4
    SHEET_ROWS = 1



sheet_url = "https://art.pixilart.com/613a60ec0bf1df1.png"
BG_IMG = simplegui.load_image(sheet_url)
BG_SHEET_WIDTH = BG_IMG.get_width()
BG_SHEET_HEIGHT = BG_IMG.get_height()


class Spritesheet:
    def __init__(self, imgURL, rows, columns, num_frames):
        self.img = simplegui.load_image(imgURL)
        sheetWIDTH = self.img.get_width()
        sheetHEIGHT = self.img.get_height()
        self.frameDimensions = (sheetWIDTH / columns, sheetHEIGHT / rows)
        self.clock = Clock()
        self.frameCenters = []
        self.currFrame = 0
        self.lastFrame = False

        for y in range(rows):
            for x in range(columns):
                temp_x = (sheetWIDTH / columns) * x
                temp_y = (sheetHEIGHT / rows) * y
                if (len(self.frameCenters) < num_frames):
                    self.frameCenters.append((temp_x + (sheetWIDTH / columns / 2), temp_y + (sheetHEIGHT / rows / 2)))

    def draw(self, canvas, pos, direction, moving):
        self.clock.tick()
        canvas.draw_image(self.img, self.frameCenters[self.currFrame], self.frameDimensions, (pos.x, pos.y), (64, 64))
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

class Item:
    def __init__(self, img, rows, columns, pos, itemIndex):
        self.img = img
        self.pos = pos
        sheetWIDTH = self.img.get_width()
        sheetHEIGHT = self.img.get_height()
        self.frameDimensions = (sheetWIDTH / columns, sheetHEIGHT / rows)
        self.frameCenters = []
        self.itemIndex = itemIndex
        self.width = 64
        self.height = 64
        
        for i in range(columns):
            x_coord = (sheetWIDTH / columns) * i
            self.frameCenters.append((x_coord + sheetWIDTH/columns/2, sheetHEIGHT/2))
            print(x_coord, sheetHEIGHT/2)
        """
        if itemName == 'sword':
            self.itemIndex = 0
        elif itemName == 'confuse':
            self.itemIndex = 1
        elif itemName == 'freeze':
            self.itemIndex = 2
        elif itemName == 'death':
            self.itemIndex = 3
        elif itemName == 'speed':
            self.itemIndex = 4
        elif itemName =='health':
            self.itemIndex = 5
        """
            
    def draw(self, canvas):
        canvas.draw_image(self.img, self.frameCenters[self.itemIndex], self.frameDimensions, (self.pos.x, self.pos.y), (128, 128))
    
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
        # self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)

    def update_pos(self):
        self.pos += self.vel

    def draw(self, canvas):
        canvas.draw_circle((self.pos.x, self.pos.y), self.width, 1, "blue", "blue")


# keyboard handler
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

        self.moving = False  # is player moving
        self.attacking = False  # is player attacking

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

        if not (self.w or self.a or self.s or self.d):
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
        self.speed = speed / 10
        self.chase = False

        self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
        self.moving = False

        self.direction_list = ["left", "right", "up", "down", "stop"]

    def update_pos(self, player):
        # decide if enemy should change direction
        if (random.randint(1, 50) == 50):
            self.direction = self.direction_list[random.randint(0, 4)]

        self.chase_check(player)

        # move enemy vel
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
            elif self.direction == "stop":  # enemy is stopped
                self.vel = Vector(0, 0)
                self.moving = False

        # check not out of bounds
        if (self.pos.x > CANVAS_WIDTH - self.width):  # stuck on right wall
            if self.vel.x > 0:
                self.vel.x = 0
                self.direction = "left"
        elif (self.pos.x < 0 + self.width):  # stuck on left wall
            if self.vel.x < 0:
                self.vel.x = 0
                self.direction = "right"
        if (self.pos.y > CANVAS_HEIGHT - self.height):  # stuck on bottom
            if self.vel.y > 0:
                self.vel.y = 0
                self.direction = "up"
        elif (self.pos.y < 0 + self.height):  # stuck on top
            if self.vel.y < 0:
                self.vel.y = 0
                self.direction = "down"

        # move enemy pos
        self.pos += self.vel
        self.vel *= 0.8

    def draw(self, canvas):
        self.spritesheet.draw(canvas, self.pos, self.direction, self.moving)

    def chase_check(self, object):
        range = 200
        xOverlap = (((self.pos.x - self.width) - range) < ((object.pos.x + object.width) + range)) and (
                ((self.pos.x + self.width) + range) > ((object.pos.x - object.width) - range))
        yOverlap = (((self.pos.y - self.height) - range) < ((object.pos.y + object.height) + range)) and (
                ((self.pos.y + self.height) + range) > ((object.pos.y - object.height) - range))
        if (xOverlap and yOverlap):
            self.chase = True
        return self.chase


class Player:
    def __init__(self, pos, vel, direction, health, max_health, damage, speed, width, height, spritesheetImage):
        self.pos = pos
        self.vel = vel
        self.direction = direction
        self.speed = speed / 10
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.hurt = False
        hurt_imgUrl = "https://cdn.discordapp.com/attachments/889956680480206888/951062203618967583/Hero-Hurt.png"

        self.width = width
        self.height = height

        self.moving = False
        self.spritesheet = Spritesheet(spritesheetImage, 4, 2, 8)
        self.hurtSpriteSheet = Spritesheet(hurt_imgUrl, 4, 2, 8)

        self.can_shoot = False  # can player shoot
        self.shootTiming = 50
        self.clock = Clock()

    def update_pos(self):
        # check not out of bounds
        if (self.pos.x > CANVAS_WIDTH - self.width):  # stuck on right wall
            if self.vel.x > 0:
                self.vel.x = 0
        elif (self.pos.x < 0 + self.width):  # stuck on left wall
            if self.vel.x < 0:
                self.vel.x = 0

        if (self.pos.y > CANVAS_HEIGHT - self.height):  # stuck on bottom
            if self.vel.y > 0:
                self.vel.y = 0
        elif (self.pos.y < 0 + self.height):  # stuck on top
            if self.vel.y < 0:
                self.vel.y = 0

        # move player pos
        self.pos += self.vel
        self.vel *= 0.8

        if not self.can_shoot:
            self.clock.tick()
            if (self.clock.transition(self.shootTiming)):
                self.can_shoot = True

    def draw(self, canvas):
        if self.hurt:
            self.hurtSpriteSheet.draw(canvas, self.pos, self.direction, self.moving)
        else:
            self.spritesheet.draw(canvas, self.pos, self.direction, self.moving)


def mouse_handler(position):
    global Mouse
    Mouse1.set_position(position)


class Mouse:

    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position


# ----------------

class Map:
    def __init__(self, imgurl, width, height, columns, rows):
        self.img = imgurl
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        # 4 frames/maps, will return a random frame
        self.frame_index = random.randint(0, 3)
        # self.frame_index = 3

        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

    def draw(self, canvas):
        # calculate the values for the canvas drawer:

        # centre of each frame, given (x, y)
        centre_source = (self.frame_width * self.frame_index + self.frame_centre_x, self.frame_centre_y)

        # pair of integers giving the size of the original image
        source_size = (self.frame_width, self.frame_height)
        # source_size = (CANVAS_DIM[0], CANVAS_DIM[1])

        # is a pair of screen coordinates specifying where the center of the image should be drawn on the canvas
        # centre_dest = (self.display_x, self.display_y)
        # centre_dest = (self.frame_centre_x, self.frame_centre_y)
        centre_dest = (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)

        # a pair of integers giving the size of how the images should be drawn
        size_dest = (CANVAS_WIDTH, CANVAS_HEIGHT)

        # draw the image
        canvas.draw_image(self.img, centre_source, source_size, centre_dest, size_dest)


# ----------------

class Interaction:
    def __init__(self, player, keyboard, mouse, enemy_list, full_heart, empty_heart, game_map):
        self.game_map = game_map
        self.player = player
        self.keyboard = keyboard
        self.enemy_list = enemy_list
        self.itemImage = simplegui.load_image("https://github.com/KoriKosmos/CS1822-Programming-Laboratory-Game/blob/main/Items.png?raw=true")
        self.item_list = []
        self.score = 0
        self.final_score = 0
        self.mouse = mouse
        self.clock = Clock()
        self.gameState = 'menu'
        self.lastClickPos = (0, 0)
        self.lastHurttime = 0
        global player_bullet
        global enemy_bullet

        self.full_heart = full_heart
        self.empty_heart = empty_heart

    def draw(self, canvas):
        if self.gameState == 'menu':
            self.menuDraw(canvas)
        elif self.gameState == 'instructions':
            self.instructions(canvas)
        elif self.gameState == 'play':
            self.playDraw(canvas)
        elif self.gameState == "over":
            self.overDraw(canvas)
            
    def instructions(self, canvas):
        canvas.draw_text('How to play: ', [310, 120], 80, "Red")
        canvas.draw_text('The objective is to survive the onslaught of demons', [110, 240], 40, "Red")
        canvas.draw_text('Use the WASD keys to move', [110, 340], 40, "Red")
        canvas.draw_text('Use the arrow keys to fire your weapon', [110, 440], 40, "Red")
        canvas.draw_text('Gain points for every demon you destroy', [110, 540], 40, "Red")
        canvas.draw_text('click anywhere to play', [320, 680], 50, "Gray")
        self.player.hurt = False

        if self.lastClickPos != self.mouse.get_position():
            self.lastClickPos = self.mouse.get_position()
            self.gameState = 'play'


    def overDraw(self, canvas):
        canvas.draw_image(BG_IMG,
                          (BG_SHEET_WIDTH / 2, BG_SHEET_HEIGHT / 2),
                          (BG_SHEET_WIDTH, BG_SHEET_HEIGHT),
                          (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2),
                          (CANVAS_WIDTH, CANVAS_HEIGHT))

        canvas.draw_text('Game Over', [310, 120], 100, "Red")
        canvas.draw_text('Your score was: ' + str(self.final_score), [350, 200], 50, "Red")
        canvas.draw_text('click anywhere to return to menu', [220, 680], 50, "Gray")
        self.player.hurt = False

        if self.lastClickPos != self.mouse.get_position():
            self.lastClickPos = self.mouse.get_position()
            self.gameState = 'menu'

    def menuDraw(self, canvas):
        canvas.draw_image(BG_IMG,
                          (BG_SHEET_WIDTH / 2, BG_SHEET_HEIGHT / 2),
                          (BG_SHEET_WIDTH, BG_SHEET_HEIGHT),
                          (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2),
                          (CANVAS_WIDTH, CANVAS_HEIGHT))
        canvas.draw_text('Tales Of Zelmore', [210, 120], 100, "Red")
        canvas.draw_text('The howls of demons resound before you', [150, 200], 50, "Red")
        canvas.draw_text('click anywhere to play', [340, 680], 50, "Gray")

        if self.lastClickPos != self.mouse.get_position():
            self.lastClickPos = self.mouse.get_position()
            self.gameState = 'instructions'

    def playDraw(self, canvas):
        self.update()  # update positions
        if Maps.map_count <= 3:
            self.game_map.draw(canvas)
            Maps.map_count += 1
        self.game_map.draw(canvas)
        # draw bullets
        for i in player_bullet:
            i.draw(canvas)

        # draw enemies
        for i in enemy_list:
            i.draw(canvas)

        self.player.draw(canvas)  # draw player
        self.clock.tick()

        if self.clock.transition(60):
            randPos = Vector(random.randrange(0, CANVAS_WIDTH), random.randrange(0, CANVAS_HEIGHT))
            new_enemy = Enemy(randPos, Vector(0, 0), "stop", 100, 4, 30, 50, enemy_url)
            if not new_enemy.chase_check(self.player):
                enemy_list.append(new_enemy)

        # draw health on screen
        self.draw_health(canvas)
        
        # draw items
        for item in self.item_list:
            item.draw(canvas)

        # draw score on screen
        canvas.draw_text("Score:" + str(self.score), (400, 50), 50, 'Red', 'monospace')

    def draw_health(self, canvas):
        offset = 0
        hearts = self.player.max_health // 50
        full_hearts = self.player.health // 50
        for i in range(full_hearts):
            canvas.draw_image(self.full_heart, (32, 32), (64, 64), (50 + offset, 50), (64, 64))
            offset += 68
        for i in range(hearts - full_hearts):
            canvas.draw_image(self.empty_heart, (32, 32), (64, 64), (50 + offset, 50), (64, 64))
            offset += 68

    def update(self):
        global enemy_list
        global player_bullet
        # check if player is dead
        if self.player.health <= 0:
            # reset game to initial conditions
            print("Game Over")
            self.player.health = self.player.max_health
            # self.gameState = "menu"
            self.gameState = "over"
            self.final_score = self.score
            self.score = 0
            self.player.pos = Vector(100, 360)
            remove_list = []
            # remove enemies on screen
            for i in enemy_list:
                remove_list.append(i)
            for i in remove_list:
                enemy_list.remove(i)
            add_enemies()  # add default enemies

        # give player vel based on wasd
        if self.keyboard.w:
            self.player.direction = "up"  # player moving up
            self.player.vel += Vector(0, -self.player.speed)
        if self.keyboard.a:
            self.player.direction = "left"
            self.player.vel += Vector(-self.player.speed, 0)
        if self.keyboard.s:
            self.player.direction = "down"
            self.player.vel += Vector(0, self.player.speed)
        if self.keyboard.d:
            self.player.direction = "right"
            self.player.vel += Vector(self.player.speed, 0)
        self.player.moving = self.keyboard.moving  # is player moving or not

        if self.player.can_shoot:
            if self.keyboard.left:  # player is shooting left
                player_bullet.append(
                    Bullet(self.player.pos, self.player.vel / 3 + Vector(-4, 0), self.player.damage, "", 5))
                self.player.direction = "left"
                self.player.can_shoot = False
            elif self.keyboard.right:  # player is shooting right
                player_bullet.append(
                    Bullet(self.player.pos, self.player.vel / 3 + Vector(4, 0), self.player.damage, "", 5))
                self.player.direction = "right"
                self.player.can_shoot = False
            elif self.keyboard.up:  # player is shooting up
                player_bullet.append(
                    Bullet(self.player.pos, self.player.vel / 3 + Vector(0, -4), self.player.damage, "", 5))
                self.player.direction = "up"
                self.player.can_shoot = False
            elif self.keyboard.down:  # player is shooting down
                player_bullet.append(
                    Bullet(self.player.pos, self.player.vel / 3 + Vector(0, 4), self.player.damage, "", 5))
                self.player.direction = "down"
                self.player.can_shoot = False

        for i in self.enemy_list:  # update enemy positions
            i.update_pos(player)
        for i in player_bullet:  # update bullet positions
            i.update_pos()

        self.player.update_pos()  # update player position
        self.lastHurttime = self.lastHurttime // 60
        if self.clock.transition(self.lastHurttime + 180):
            self.player.hurt = False
        self.check_collisions()  # check if bullets have hit enemy/player

    def check_collisions(self):
        remove_enemy = []
        remove_bullet = []
        for bullet in player_bullet:  # check if player bullet has hit enemy
            for enemy in self.enemy_list:
                if self.collision(bullet, enemy):
                    enemy.health -= bullet.damage  # damage enemy
                    enemy.vel += bullet.vel
                    self.score += 10  # add score for hit
                    if enemy.health <= 0:  # check if enemy is dead
                        remove_enemy.append(enemy)
                        ranNum = random.randrange(0,3)
                        if ranNum == 0:
                            ranNum = random.randrange(0,5)
                            newItem = Item(self.itemImage, 1, 6, enemy.pos, ranNum)
                            self.item_list.append(newItem)
                        self.score += 100  # add score for kill
                    remove_bullet.append(bullet)

        # check if enemy hits player
        for enemy in self.enemy_list:
            if self.collision(self.player, enemy) and not self.player.hurt:
                remove_enemy.append(enemy)
                self.player.health -= 50
                self.player.hurt = True
                self.lastHurtTime = self.clock.time
                
        for item in self.item_list:
            if self.collision(self.player, item):
                if item.itemIndex == 0:
                    self.player.shootTiming -= 5
                    if self.player.shootTiming < 20:
                        self.player.shootTiming = 20
                if item.itemIndex == 1:
                    self.player.max_health += 1
                if item.itemIndex == 2:
                    for enemy in self.enemy_list:
                        enemy.vel = Vector(0,0)
                if item.itemIndex == 3:
                    for enemy in self.enemy_list:
                        remove_enemy.append(enemy)
                if item.itemIndex == 4:
                    self.player.speed += 0.1
                    if self.player.speed > 1:
                        self.player.speed = 1
                if item.itemIndex == 5:
                    self.player.health += 50
                self.item_list.remove(item)
                       
                    

        # check if bullet is offscreen
        for i in player_bullet:
            xpos = i.pos.x
            ypos = i.pos.y
            if xpos < 0 or ypos < 0 or xpos > CANVAS_WIDTH or ypos > CANVAS_HEIGHT:
                if i not in remove_bullet:
                    remove_bullet.append(i)

        # clean up bullets and enemies
        for item in remove_enemy:
            if item in enemy_list:
                self.enemy_list.remove(item)
        for item in remove_bullet:
            if item in player_bullet:
                player_bullet.remove(item)

    def collision(self, object1, object2):
        xOverlap = (((object1.pos.x - object1.width) < (object2.pos.x + object2.width)) and (
                (object1.pos.x + object1.width) > (object2.pos.x - object2.width)))
        yOverlap = (((object1.pos.y - object1.height) < (object2.pos.y + object2.height)) and (
                (object1.pos.y + object1.height) > (object2.pos.y - object2.height)))
        return xOverlap and yOverlap


sound = simplegui.load_sound(
    'https://github.com/KoriKosmos/CS1822-Programming-Laboratory-Game/blob/main/YouSayRun(8%20bit).ogg?raw=true')
sound.play()
# INITIALISATION
player_bullet = []
enemy_bullet = []
enemy_list = []

# add enemies to enemy list
enemy_url = "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Flame_Oni.png"


def add_enemies():
    global enemy_list
    enemy_list.append(Enemy(Vector(1000, 500), Vector(0, 0), "stop", 100, 4, 30, 50, enemy_url))
    enemy_list.append(Enemy(Vector(1000, 200), Vector(0, 0), "stop", 100, 4, 30, 50, enemy_url))
    enemy_list.append(Enemy(Vector(1000, 400), Vector(0, 0), "stop", 100, 4, 60, 50, enemy_url))
    enemy_list.append(Enemy(Vector(1000, 300), Vector(0, 0), "stop", 100, 4, 30, 50, enemy_url))


add_enemies()

keyboard = Keyboard()

spritesheetImage = 'https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Hero_Vertical.png'
player = Player(Vector(100, 360), Vector(0, 0), "right", 150, 150, 50, 5, 30, 30, spritesheetImage)
Mouse1 = Mouse((0, 0))

# ----------------
game_map = Map(
    Maps.IMG,
    Maps.SHEET_WIDTH,
    Maps.SHEET_HEIGHT,
    Maps.SHEET_COLUMNS,
    Maps.SHEET_ROWS
)
# ----------------

full_heart = simplegui.load_image(
    "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Heart.png")
empty_heart = simplegui.load_image(
    "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Heart-hurt.png")
# interaction = Interaction(player, keyboard, Mouse1, enemy_list, full_heart, empty_heart)

interaction = Interaction(player, keyboard, Mouse1, enemy_list, full_heart, empty_heart, game_map)

# create frame
frame = simplegui.create_frame("Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)
frame.set_canvas_background('#004D26')  # set background color
# Mouse handler
frame.set_mouseclick_handler(mouse_handler)
# keyboard handler
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)

frame.start()
