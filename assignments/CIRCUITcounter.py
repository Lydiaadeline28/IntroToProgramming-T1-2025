from adafruit_circuitplayground import cp
import time

count = 0

while True:
    if cp.button_a and count < 10:
        cp.pixels[count] = (0, 50, 0)
        count += 1
        time.sleep(0.2)

    if cp.button_b and count > 0:
        count -= 1
        cp.pixels[count] = (0, 0, 0)
        time.sleep(0.2)
