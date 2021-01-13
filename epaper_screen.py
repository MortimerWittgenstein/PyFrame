from IT8951.display import AutoEPDDisplay
from IT8951 import constants
from PIL import Image

class EPaper:
    def displayImage(self, image):
        content = Image.open(image)

        # auto rotate depending on aspect ratio
        if content.width > content.height:
            rotation = None
        else:
            rotation = 'CW'

        # init screen; use vcom value of your screen
        screen = AutoEPDDisplay(vcom=-2.13, rotate=rotation)

        # make screen clear
        #screen.clear()

        # shrink image if necessary
        screen_dims = (screen.width, screen.height)
        content.thumbnail(screen_dims)

        # align image in center of screen
        paste_coords = [int((screen_dims[i] - content.size[i]) / 2) for i in (0,1)]

        screen.frame_buf.paste(content, paste_coords)

        # display the image
        screen.draw_full(constants.DisplayModes.GC16)