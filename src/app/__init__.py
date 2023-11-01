from flask import Flask
app = Flask(__name__)

def create_app():
    return app

@app.route("/")
def hello():
    return "hello world from DevContainer"