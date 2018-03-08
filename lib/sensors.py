from lib.am2320 import AM2320
from tsl2561 import TSL2561


def read_sensors():

    # Get temperature and humidity values from AM2320
    am2320 = AM2320(1)
    (temp, humi) = am2320.readSensor()

    # Get luminosity from TSL2561
    tsl = TSL2561(debug=1)
    lux = tsl.lux()

    return (temp, humi, lux, soil)
