#//usr/bin/env python3

from lib.am2320 import AM2320
from tsl2561 import TSL2561

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306

from datetime import datetime
import time
import sys
import os
import requests

serial = spi(gpio_DC=27, gpio_RST=22)
device = ssd1306(serial)

if __name__ == '__main__':

    now = datetime.now().isoformat()
    # Get temperature and humidity values from AM2320
    am2320 = AM2320(1)
    (temp, humi) = am2320.readSensor()

    # Get luminosity from TSL2561
    tsl = TSL2561(debug=1)
    lux = tsl.lux()

    # Send data
    url = os.environ['SERVER_URL'] + '/readings'
    token = os.environ['TOKEN']
    payload = {
        'date': now,
        'temp': temp,
        'humi': humi,
        'lux': lux
    }
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/json'
    }
    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        # Print on OLED screen
        with canvas(device) as draw:
            string = ('{}:\nTemperature: {} C,\nHumidity: {}%,\nLuminosity: {} lux'
                      .format(now, temp, humi, lux))
            draw.text((0, 0), string, fill="white")
        time.sleep(15)
        sys.exit(0)
    else:
        r.raise_for_status()
        sys.exit(1)
