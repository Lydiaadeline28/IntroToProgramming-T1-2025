from adafruit_circuitplayground import cp
import time

while True:
    cp.pixels.fill((255, 0, 0))   # red
    cp.play_tone(500, 0.5)        # 500ms
    cp.pixels.fill((0, 0, 255))   # blue
    cp.play_tone(900, 0.5)
    