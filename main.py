#//usr/bin/env python3

from datetime import datetime
import sys
import os
import requests

from lib.display import display_data
from lib.sensors import read_sensors

if __name__ == '__main__':
    now = datetime.now().isoformat()
    temp, humi, lux, soil = read_sensors()

    # Send data
    url = os.environ['SERVER_URL'] + '/readings'
    token = os.environ['TOKEN']
    payload = {
        'date': now,
        'temp': temp,
        'humi': humi,
        'lux': lux,
        'soil': soil
    }
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/json'
    }
    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        display_data(now, temp, humi, lux, soil)
        sys.exit(0)
    else:
        r.raise_for_status()
        sys.exit(1)
