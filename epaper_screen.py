from IT8951.display import AutoEPDDisplay
from IT8951 import constants
from PIL import Image

class EPaper:
    def displayImage(self, path, bgColor=0xffffff):
        content = Image.open(path)

        # auto rotate depending on screen size
        if content.width > content.height:
            rotation = None
        else:
            rotation = 'CW'

        screen = AutoEPDDisplay(vcom=-2.47, rotate=rotation)

        # make screen clear
        screen.clear()

        screen.frame_buf.paste(0xFF, box=(0, 0, screen.width, screen.height))
        dims = (screen.width, screen.height)
        content.thumbnail(dims)

        # set background color
        img = Image.new("RGB", dims, bgColor)

        # align image with bottom of screen
        paste_coords = [int((dims[i] - content.size[i]) / 2) for i in (0,1)]
        img.paste(content, paste_coords)

        screen.frame_buf.paste(img, (0, 0))

        # display the image
        screen.draw_full(constants.DisplayModes.GC16)