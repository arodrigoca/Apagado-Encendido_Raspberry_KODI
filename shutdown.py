import sys
sys.path.append('/scripts/.kodi/addons/python.RPi.GPIO/lib')
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(05, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    print GPIO.input(05)
    if(GPIO.input(05) == False):
        os.system("sudo shutdown -h now")
        break
    time.sleep(1)
