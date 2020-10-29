# Add your Python code here. E.g.
from microbit import *
import speech
import random

lengtewoordarray = 3

#arrays met woorden
onderwerp = ["She", "Guido", "Rosmerta"]
werkwoord = ["walks", "learns", "drinks"]
rest = ["hard", "at school", "coffee"]


def saythewords1(word):
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)
    
def saythewords2():
    willekeuriggetal = random.randint(0, lengtewoordarray - 1)
    display.show(willekeuriggetal)
    saythewords1(onderwerp[willekeuriggetal])
    saythewords1(werkwoord[willekeuriggetal])
    saythewords1(rest[willekeuriggetal])

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        saythewords1("Hello im happy")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        saythewords1("why are you sad")
    elif display.read_light_level() < 40:
        saythewords2()
    elif button_a.is_pressed() < 2:
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        print("x, y, z:", x, y, z)
        sleep(500)
    else:
        display.show(Image.SQUARE)
        
    
    
    