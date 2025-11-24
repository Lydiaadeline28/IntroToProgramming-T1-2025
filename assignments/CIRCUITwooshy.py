from adafruit_circuitplayground import cp
import time


while True:
    if cp.button_a:
        for i in range(10):
            cp.pixels[i] = (0, 50, 0)   # turn pixel on (green)
            time.sleep(0.1)             # 100ms
            cp.pixels[i] = (0, 0, 0)    # turn pixel off
            time.sleep(0.1)             # 100ms
