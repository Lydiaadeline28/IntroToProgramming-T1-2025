from adafruit_circuitplayground import cp
import time

while True:
    x, y, z = cp.acceleration

    # LEFT
    if x < 0:
        cp.pixels[1] = (0, 255, 0)
        cp.pixels[2] = (0, 255, 0)
        cp.pixels[3] = (0, 255, 0)

        cp.pixels[6] = (0, 0, 0)
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)

    # RIGHT
    else:
        cp.pixels[6] = (255, 0, 0)
        cp.pixels[7] = (255, 0, 0)
        cp.pixels[8] = (255, 0, 0)

        cp.pixels[1] = (0, 0, 0)
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)

    time.sleep(0.05)