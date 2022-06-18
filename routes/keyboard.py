from pynput.keyboard import Controller
from flask import Blueprint, request
from lib import special_to_key

keyboard = Controller()

hub = Blueprint('keyboard', __name__)

def get_key():
    try:
        is_special = True if request.args.get("special") == "true" else False
    except Exception:
        is_special = False
    
    key = request.args.get('key')
    
    if(is_special): key = special_to_key(key)

    return key


@hub.route('/press')
def press():
    key = get_key()

    keyboard.press(key)
    return '{"status": "OK"}'

@hub.route('/release')
def release():
    key = get_key()

    keyboard.release(key)
    return '{"status": "OK"}'

@hub.route('/pr')
def pr():
    key = get_key()
    
    keyboard.press(key)
    keyboard.release(key)
    return '{"status": "OK"}'

@hub.route('/type')
def type():
    try:
        text = request.args.get('text')
    except Exception:
        return '{"status": "Error", "error": "Missing \\"type\\" parameter."}'

    keyboard.type(text)
    return '{"status": "OK"}'