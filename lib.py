from pynput.keyboard import Key
from pynput.mouse import Button

def special_to_key(special):
    try:
        return Key[special]
    except Exception:
        return None

def key_to_special(key):
    for k, v in Key.__members__.items():
        if(v == key):
            return k
    return None

def special_to_button(special):
    try:
        return Button[special]
    except Exception:
        return None

def button_to_special(button):
    for k, v in Button.__members__.items():
        if(v == button):
            return k
    return None
