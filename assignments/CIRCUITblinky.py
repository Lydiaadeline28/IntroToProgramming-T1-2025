import time
from adafruit_circuitplayground import cp

INTERVAL = 0.367  # 367 ms

while True:
    # Turn  green
    cp.pixels.fill((0, 255, 0))
    cp.pixels.show()
    time.sleep(INTERVAL)

    # Turn  off
    cp.pixels.fill((0, 0, 0))
    cp.pixels.show()
    time.sleep(INTERVAL)
