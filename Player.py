try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Player:
    def __init__(self, moving_character, bullet, health, damage, speed):
        self.moving_character = moving_character
        self.health = health
        self.damage = damage
        self.speed = speed

    def draw(self, canvas):
        self.moving_character.draw(canvas)
    
    def update_pos(self):
        self.moving_character.update_pos()