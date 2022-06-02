from pynput.keyboard import Controller
from flask import Flask, request
from lib import special_to_key


keyboard = Controller()


app = Flask(__name__)

#app.opts = {}
#app.opts['title'] = 'Page'

#app.static_folder_path = os.path.join(app.root_path, 'static')

@app.route('/')
def index():
    return "Ready!"


# KEYBOARD




@app.route('/press')
def press():
    try:
        is_special = True if request.args.get("special") == "true" else False
    except Exception:
        is_special = False
    
    try:
        key = request.args.get('key')
    except Exception:
        return '{"status": "Error", "error": "Missing \\"key\\" parameter."}'

    if(is_special): key = special_to_key(key)

    keyboard.press(key)
    return '{"status": "OK"}'

@app.route('/release')
def release():
    try:
        is_special = True if request.args.get("special") == "true" else False
    except Exception:
        is_special = False
    
    try:
        key = request.args.get('key')
    except Exception:
        return '{"status": "Error", "error": "Missing \\"key\\" parameter."}'

    if(is_special): key = special_to_key(key)

    keyboard.release(key)
    return '{"status": "OK"}'

@app.route('/pr')
def pr():
    try:
        is_special = True if request.args.get("special") == "true" else False
    except Exception:
        is_special = False
    
    try:
        key = request.args.get('key')
    except Exception:
        return '{"status": "Error", "error": "Missing \\"key\\" parameter."}'

    if(is_special): key = special_to_key(key)

    keyboard.press(key)
    keyboard.release(key)
    return '{"status": "OK"}'

@app.route('/type')
def type():
    try:
        text = request.args.get('text')
    except Exception:
        return '{"status": "Error", "error": "Missing \\"type\\" parameter."}'

    keyboard.type(text)
    return '{"status": "OK"}'

# MOUSE



#start flask server
if __name__ == "__main__":
    app.run()