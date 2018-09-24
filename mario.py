from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

pixel = 0
while pixel < 8:
    i=0
    while i < 8:
        sense.set_pixel(i, pixel, pick_random_colour())
        sleep(0.4)
        sense.clear()
        i+=1
    pixel+=1
    if pixel > 8
    pixel = 0
