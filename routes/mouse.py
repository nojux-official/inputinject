from pynput.mouse import Controller, Button
from flask import Blueprint, request
from lib import special_to_button

mouse = Controller()

hub = Blueprint('mouse', __name__)

def get_xy():
    x = request.args.get("x")
    y = request.args.get("y")
    return (x, y)


@hub.route('/press')
def press():
    try:
        mouse.position = get_xy()
    except Exception:
        pass
    
    if("button" in request.args):
        button = special_to_button(
            request.args.get("button")
        )
    else:
        button = Button.left
    
    mouse.press(button)
        
    return '{"status": "OK"}'

@hub.route('/release')
def release():
    try:
        mouse.position = get_xy()
    except Exception:
        pass
    
    if("button" in request.args):
        button = special_to_button(
            request.args.get("button")
        )
    else:
        button = Button.left
        
    mouse.release(button)
    
    return '{"status": "OK"}'

@hub.route('/click')
def click():
    try:
        mouse.position = get_xy()
    except Exception:
        pass

    if("button" in request.args):
        button = special_to_button(
            request.args.get("button")
        )
    else:
        button = Button.left
    
        
    mouse.press(button)
    mouse.release(button)
    
    return '{"status": "OK"}'

@hub.route('/scroll')
def scroll():
    try:
        mouse.position = get_xy()
    except Exception:
        pass

    vx = request.args.get("vx")
    vy = request.args.get("vy")
    
    mouse.scroll(vx, vy)
    
    return '{"status": "OK"}'

@hub.route('/move')
def move():
    try:
        relative = True if request.args.get("relative") == "true" else False
    except Exception:
        relative = False
    
    (x, y) = get_xy()

    if(relative): mouse.move(x, y)
    else: mouse.position = (x, y)
    
    return '{"status": "OK"}'