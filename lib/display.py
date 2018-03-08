from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306

import time

serial = spi(gpio_DC=27, gpio_RST=22)
device = ssd1306(serial)


def display_data(now, temp, humi, lux, soil):
    with canvas(device) as draw:
        string = '''{}
Temperature: {} C,
Humidity: {}%,
Luminosity: {} lux,
Soil: {}
'''.format(now, temp, humi, lux, soil)
        draw.text((0, 0), string, fill="white")
    time.sleep(15)
