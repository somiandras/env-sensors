from lib.am2320 import AM2320
from tsl2561 import TSL2561
import Adafruit_ADS1x15


def read_sensors():

    # Get temperature and humidity values from AM2320
    am2320 = AM2320(1)
    (temp, humi) = am2320.readSensor()

    # Get luminosity from TSL2561
    tsl = TSL2561(debug=1)
    lux = tsl.lux()

    # Get soil moisture from soil hygrometer + ADS1015
    adc = Adafruit_ADS1x15.ADS1015()
    soil = adc.read_adc(0, gain=1)

    return (temp, humi, lux, soil)
