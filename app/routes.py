from flask import Blueprint, render_template, jsonify, request
from app.model import chat_rooms
import datetime


chat = Blueprint('chat', __name__)

@chat.route('/')
def index():
    """Serve the static HTML file on the root endpoint."""
    return render_template('index.html')


@chat.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    username = request.form.get('username')
    message = request.form.get('message')
    
    if not username or not message:
        return jsonify({"error": "Both 'username' and 'message' fields are required"}), 400
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    chat_line = f"[{timestamp}] {username}: {message}"
    
    if room not in chat_rooms:
        chat_rooms[room] = []
    chat_rooms[room].append(chat_line)
    
    return jsonify({"status": "Message saved"}), 201

@chat.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    if room not in chat_rooms:
        return jsonify({"error": "Room not found"}), 404

    chat_log = "\n".join(chat_rooms[room])
    return chat_log, 200, {'Content-Type': 'text/plain; charset=utf-8'}






