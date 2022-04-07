from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, rotate=0, blocks_arranged_in_reverse_order=True)

with canvas(device) as draw:
    # Draw point
    draw.point((1, 1), fill="white")

    # Draw bar player 2
    draw.line((5, 1, 5, 3), fill="white")