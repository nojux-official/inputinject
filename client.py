from pynput import keyboard
import requests
from lib import key_to_special
from time import sleep

ADDRESS = "http://10.42.0.92:5000/"

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        requests.get(ADDRESS + "press", params={"key": key.char})
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        requests.get(ADDRESS + "press", params={"key": key_to_special(key), "special": "true"})

def on_release(key):
    try:
        print('alphanumeric key {0} released'.format(
            key.char))
        requests.get(ADDRESS + "release", params={"key": key.char})
    except AttributeError:
        print('special key {0} released'.format(
            key))
        requests.get(ADDRESS + "release", params={"key": key_to_special(key), "special": "true"})
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    sleep(0.1)
    if(not listener.running): exit()