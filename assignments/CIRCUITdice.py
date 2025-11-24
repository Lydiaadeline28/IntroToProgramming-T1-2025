import random
from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        n = random.randint(1, 10)
        cp.pixels.fill((0, 0, 0))
        for i in range(n):
            cp.pixels[i] = (255, 92, 225)
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))