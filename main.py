#//usr/bin/env python3

from lib.am2320 import AM2320
from tsl2561 import TSL2561

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
import sys
from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    # Get temperature and humidity values from AM2320
    am2320 = AM2320(1)
    (temp, humi) = am2320.readSensor()

    # Get luminosity from TSL2561
    tsl = TSL2561(debug=1)
    lux = tsl.lux()

    serial = spi(gpio_DC=27, gpio_RST=22)
    device = ssd1306(serial)

    with canvas(device) as draw:
        string = ('{}:\nTemperature: {} C,\nHumidity: {}%,\nLuminosity: {} lux'
                  .format(now, temp, humi, lux))
        draw.text((0, 0), string, fill="white")
    time.sleep(15)
    print(string.replace('\n', ' '))
    sys.exit(0)
