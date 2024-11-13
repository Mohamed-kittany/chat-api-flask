from flask import Flask
from app.routes import chat

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat)
    
    #Set a custom name for the app
    #app.name = "chat-api"
    return app
