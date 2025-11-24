import random
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
  
    if cp.shake():
        for i in range(10):
            cp.pixels[i] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        cp.pixels.show()

    time.sleep(0.05)