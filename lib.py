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

def special_to_resolution(special):
    li = special.split("x")
    li[0] = int(li[0])
    li[1] = int(li[1])
    return tuple(li)

def resolution_to_special(tupl):
    return f'{tupl[0]}x{tupl[1]}'