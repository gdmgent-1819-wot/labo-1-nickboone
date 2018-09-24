from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
sense.clear()

x = 0
y = 0
color = (0,0,0)
#with this loop is there a new arcade visible each 0.5 seconds
while True:
    on_off = random.randint(0,1)
    if on_off < 1:
        sense.set_pixel(x,y,color)
        sense.set_pixel(7-x,y,color)
    x += 1
    if x > 4:
        x = 0
        y += 1
        if y > 7:
            
            y = 0
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            
            color = (r,g,b)
            sleep(0.5)
            sense.clear()
            