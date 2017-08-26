from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from dht import DHT22

dhtPin = Pin(17)
d = DHT22(dhtPin)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

lcd = I2cLcd(i2c, 0x27, 4, 20)
lcd.clear()

d.measure()
lcd.putstr('T: {0:.2f}'.format(d.temperature()))
lcd.putstr('H: {0:.2f}'.format(d.humidity()))
