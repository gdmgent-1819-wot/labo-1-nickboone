from sense_hat import SenseHat
from time import sleep
import time
from random import randint

sense = SenseHat()

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)


# string
letters = "NMD"

#loop in string
i=0
while i< 3:
        sense.show_letter(letters[i], pick_random_colour())
        time.sleep(1)
        i+=1
        if i > 2:
            i = 0
            sleep(2)
