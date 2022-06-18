from flask import Flask
import routes.keyboard

app = Flask(__name__)

#app.opts = {}
#app.opts['title'] = 'Page'

#app.static_folder_path = os.path.join(app.root_path, 'static')

@app.route('/')
def index():
    return "Ready!"


# KEYBOAR
app.register_blueprint(routes.keyboard.hub)

# MOUSE



#start flask server
if __name__ == "__main__":
    app.run()