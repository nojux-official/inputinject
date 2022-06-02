from pynput.keyboard import Key

switcher = {
    "enter": Key.enter,
    "space": Key.space,
    "backspace": Key.backspace,
    "delete": Key.delete,
    "tab": Key.tab,
    "ctrl": Key.ctrl,
    "ctrl_l": Key.ctrl_l,
    "ctrl_r": Key.ctrl_r,
    "alt": Key.alt,
    "alt_l": Key.alt_l,
    "alt_r": Key.alt_r,
    "alt_gr": Key.alt_gr,
    "cmd": Key.cmd,
    "cmd_l": Key.cmd_l,
    "cmd_r": Key.cmd_r,
    "caps_lock": Key.caps_lock,
    "shift": Key.shift,
    "shift_l": Key.shift_l,
    "shift_r": Key.shift_r,
    "menu": Key.menu,
    "left": Key.left,
    "right": Key.right,
    "up": Key.up,
    "down": Key.down,
    "f1": Key.f1,
    "f1": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    "f5": Key.f5,
    "f6": Key.f6,
    "f7": Key.f7,
    "f8": Key.f8,
    "f9": Key.f9,
    "f10": Key.f10,
    "f11": Key.f11,
    "f12": Key.f12
}

def special_to_key(special):
    try:
        return switcher.get(special)
    except Exception:
        return None

def key_to_special(key):
    for k, v in switcher.items():
        if(v == key):
            return k
    return None
