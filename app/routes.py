from flask import Blueprint, render_template
from app.model import chat_rooms  # Import chat_rooms for potential use in routing

chat = Blueprint('chat', __name__)

@chat.route('/')
def index():
    """Serve the static HTML file on the root endpoint."""
    return render_template('index.html')