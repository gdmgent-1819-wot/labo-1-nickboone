from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
# with a press on the joystick de user roll 10 times the rolling dice's
def rollDice():
    total = 0;
    for score in range(10):
        roll = random.randint(1, 6)
        print("beurt "+ str(score+1) +": "+str(roll))
        total += roll
        if score == 9:
            print("your total is "+ str(total))
            total = 0
while True:
    for event in sense.stick.get_events():            
        if format(event.action) == "pressed":
            rollDice()