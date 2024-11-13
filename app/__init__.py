from flask import Flask
from app.routes import chat
import os


def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
    app.register_blueprint(chat)
    
    #Set a custom name for the app
    #app.name = "chat-api"
    return app
