from pynput.keyboard import Key

def special_to_key(special):
    try:
        return Key[special]
    except Exception:
        return None

def key_to_special(key):
    for k, v in Key.items():
        if(v == key):
            return k.name
    return None
