from machine import I2C
from machine import Pin

scl = Pin(22)
sda = Pin(21)
i2c = I2C(scl=scl, sda=sda, freq=100000)
i2c.scan()
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text('ESP8266', 35, 5)
oled.text('MicroPython', 20, 20)
oled.text('MicroPython', 20, 20)
oled.text('TEMP: {0:.2f}'.format(25.5), 3, 50)
oled.show()