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

def get_key():
    try:
        is_special = True if request.args.get("special") == "true" else False
    except Exception:
        is_special = False
    
    key = request.args.get('key')
    
    if(is_special): key = special_to_key(key)

    return key


@app.route('/press')
def press():
    key = get_key()

    keyboard.press(key)
    return '{"status": "OK"}'

@app.route('/release')
def release():
    key = get_key()

    keyboard.release(key)
    return '{"status": "OK"}'

@app.route('/pr')
def pr():
    key = get_key()
    
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