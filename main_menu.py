try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Keyboard import Keyboard

#CANVAS_DIMS = [600, 400]
CANVAS_DIMS = [720, 576]

title = "Game Title!"
play = "Play Game"
credits = "Credits"
quit = "Quit"

# the three positions the cursor can move to, dependent on canvas size.
play_pos = [CANVAS_DIMS[0] - 550, CANVAS_DIMS[1] / 2]
credit_pos = [CANVAS_DIMS[0] - 550, CANVAS_DIMS[1] / 2 + 60]
quit_pos = [CANVAS_DIMS[0] - 550, CANVAS_DIMS[1] / 2 + 120]

class Menu:
    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.cursor_position = [play_pos, credit_pos, quit_pos]
        # index pointer for the list
        self.position = 0


    def draw(self, canvas):
        # the text
        canvas.draw_text(title, [CANVAS_DIMS[0] / 4.5, CANVAS_DIMS[1] / 4], 80, "Blue", 'sans-serif')
        canvas.draw_text(play, [CANVAS_DIMS[0] - 450, CANVAS_DIMS[1] / 2], 40, "Red", 'sans-serif')
        canvas.draw_text(credits, [CANVAS_DIMS[0] / 2 - 60, CANVAS_DIMS[1] / 2 + 60], 40, "Red", 'sans-serif')
        canvas.draw_text(quit, [CANVAS_DIMS[0] / 2 - 40, CANVAS_DIMS[1] / 2 + 120], 40, "Red", 'sans-serif')
        #  the cursor
        canvas.draw_text(">", self.cursor_position[self.position], 40, "Green", 'sans-serif')


    def move_cursor(self):
        if self.keyboard.down or self.keyboard.s:
            pass
        if self.keyboard.up or self.keyboard.w:
            pass

    def select(self):
        # need to initialise space/enter in keyboard class
        pass

    def update(self):
        self.move_cursor()
        self.select()


kbd = Keyboard()
game_menu = Menu(kbd)


def draw(canvas):
    game_menu.update()
    game_menu.draw(canvas)


frame = simplegui.create_frame('Menu', CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_canvas_background('White')
frame.start()