import time
from MusicController import *
from Displays import *

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
mydisplay.showText('That was fun!')

MusicController().run()

