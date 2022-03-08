try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

sheet_url = "https://raw.githubusercontent.com/KoriKosmos/CS1822-Programming-Laboratory-Game/main/Fantasy%20Wooden%20Floor.png"
IMG = simplegui.load_image(sheet_url)
SHEET_WIDTH = IMG.get_width()
SHEET_HEIGHT = IMG.get_height()
SHEET_COLUMNS = 4
SHEET_ROWS = 1

CANVAS_DIM = [480, 480]


class Map:
    def __init__(self, imgurl, width, height, columns, rows):
        self.img = imgurl
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        # 4 frames/maps, will return a random frame
        self.frame_index = random.randint(0, 3)

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

        # is a pair of screen coordinates specifying where the center of the image should be drawn on the canvas
        # centre_dest = (self.display_x, self.display_y)
        centre_dest = (self.frame_centre_x, self.frame_centre_y)

        # a pair of integers giving the size of how the images should be drawn
        size_dest = (CANVAS_DIM[0], CANVAS_DIM[1])

        # draw the image
        canvas.draw_image(self.img, centre_source, source_size, centre_dest, size_dest)


game_map = Map(
    IMG,
    SHEET_WIDTH,
    SHEET_HEIGHT,
    SHEET_COLUMNS,
    SHEET_ROWS
)

frame = simplegui.create_frame("Map", CANVAS_DIM[0], CANVAS_DIM[1])
frame.set_draw_handler(game_map.draw)
frame.start()

