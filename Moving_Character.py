try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Moving_Character:
    def __init__(self, pos, vel, spritesheet, direction_facing):
        self.pos = pos
        self.vel = vel
        self.spritesheet = spritesheet
        self.direction_facing = direction_facing

    def draw(self, canvas):
        #spritesheet.draw()
        canvas.draw_circle((self.pos.x, self.pos.y), 30, 1, "Blue", "Blue")

    def update_pos(self):
        self.pos += self.vel
        self.vel *= 0.8