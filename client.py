from pynput import keyboard, mouse
import requests
from lib import key_to_special
from time import sleep

ADDRESS = "http://10.42.0.92:5000/"


#KEYBOARD

def on_key_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        requests.get(ADDRESS + "keyboard/press", params={"key": key.char})
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        requests.get(ADDRESS + "keyboard/press", params={"key": key_to_special(key), "special": "true"})

def on_key_release(key):
    try:
        print('alphanumeric key {0} released'.format(
            key.char))
        requests.get(ADDRESS + "keyboard/release", params={"key": key.char})
    except AttributeError:
        print('special key {0} released'.format(
            key))
        requests.get(ADDRESS + "keyboard/release", params={"key": key_to_special(key), "special": "true"})
    if key == keyboard.Key.esc:
        # Stop listener
        return False


#MOUSE

def on_mouse_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    requests.get(ADDRESS + "mouse/move", params={"x": x, "y": y})

def on_button_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

    if(pressed):
        requests.get(ADDRESS + "mouse/press", params={"x": x, "y": y})
    else:
        requests.get(ADDRESS + "mouse/release", params={"x": x, "y": y})

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    requests.get(ADDRESS + "mouse/scroll", params={"x": x, "y": y, "dx": dx, "dy": dy})



#LISTENERS

k_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release)
k_listener.start()

m_listener = mouse.Listener(
    on_move=on_mouse_move,
    on_click=on_button_click,
    on_scroll=on_scroll)
m_listener.start()

while True:
    sleep(0.1)
    if(not k_listener.running): exit()
    if(not k_listener.running): exit()