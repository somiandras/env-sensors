Get temperature, humidity and luminosity sensor values on Raspberry Pi and print it to the 128x64 OLED display and also upload them to an API endpoint.

Simple Python script based on libraries for interacting with the sensors.

__Hardware:__

- Raspberry Pi Zero (Raspbian Stretch)
- AM2320 - temperature/humidity sensor
- TSL2561 - Luminosity sensor
- SSD1306 - 128x64 OLED display

__Python libraries:__

- [am2320](https://github.com/Gozem/am2320)
- [tsl2561](https://github.com/sim0nx/tsl2561) 
- [luma.oled](https://github.com/rm-hull/luma.oled)

[Here's a simple server](https://github.com/somiandras/pi-sensors-server) for uploading, storing and retrieving the data.