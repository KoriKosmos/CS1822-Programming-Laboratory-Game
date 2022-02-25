try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

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