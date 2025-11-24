import time
from adafruit_circuitplayground import cp


while True:
    temp = cp.temperature  # Convert C → F


    cp.pixels.fill((0, 0, 0))

    # Pixel 0
    if temp < 78:
        cp.pixels[0] = (0, 0, 1)

    # Pixel 1
    if temp > 78:
        cp.pixels[1] = (0, 0, 1)

    # Pixel 2
    if temp > 79:
        cp.pixels[2] = (0, 0, 1)

    # Pixel 3
    if temp > 80:
        cp.pixels[3] = (1, 1, 0)

    # Pixel 4
    if temp > 81:
        cp.pixels[4] = (1, 1, 0)

    # Pixel 5
    if temp > 82:
        cp.pixels[5] = (1, 1, 0)

    # Pixel 6
    if temp > 83:
        cp.pixels[6] = (1, 1, 0)

    # Pixel 7
    if temp > 84:
        cp.pixels[7] = (1, 0, 0)

    # Pixel 8
    if temp > 85:
        cp.pixels[8] = (1, 0, 0)

    # Pixel 9
    if temp> 86:
        cp.pixels[9] = (1, 0, 0)

    time.sleep(0.2)