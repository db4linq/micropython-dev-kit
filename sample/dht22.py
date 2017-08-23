import time
from dht import DHT22
from machine import Pin, Timer

dhtPn = Pin(17)
d = DHT22(dhtPn)

tim0 = Timer(0)

def callback():
    d.measure()
    print(d.temperature(), d.humidity()) 

tim0.init(period=5000, mode=Timer.PERIODIC, callback=lambda t:callback())

    

