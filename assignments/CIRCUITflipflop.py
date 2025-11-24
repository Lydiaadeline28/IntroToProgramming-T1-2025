import time
from adafruit_circuitplayground import cp

GREEN = (0, 255, 0)
OFF = (0, 0, 0)

while True:
    cp.pixels[0:5], cp.pixels[5:10] = ([GREEN]*5, [OFF]*5) if cp.switch else ([OFF]*5, [GREEN]*5)
    cp.pixels.show()
    time.sleep(0.05)
    