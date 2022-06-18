from flask import Flask
import routes.keyboard
import routes.mouse

app = Flask(__name__)

#app.opts = {}
#app.opts['title'] = 'Page'

#app.static_folder_path = os.path.join(app.root_path, 'static')

@app.route('/')
def index():
    return "Ready!"

# KEYBOARD
app.register_blueprint(routes.keyboard.hub, url_prefix="/keyboard")

# MOUSE
app.register_blueprint(routes.mouse.hub, url_prefix="/mouse")


#start flask server
if __name__ == "__main__":
    app.run()