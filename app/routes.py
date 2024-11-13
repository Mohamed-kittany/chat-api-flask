from flask import Blueprint, render_template, jsonify, request
from app.model import chat_rooms
#import datetime


chat = Blueprint('chat', __name__)


############################### GET '/' ###############################
@chat.route('/')
def index():
    """Serve the static HTML file on the root endpoint."""
    return render_template('index.html')


############################### POST /api/chat/<room> ###############################
@chat.route('/api/chat/<room>', methods=['POST'])
def post_message(room):
    
    username = request.form.get('username')
    message = request.form.get('msg')

    if not username or not message:
        return jsonify({"error": "Both 'username' and 'message' fields are required"}), 400
    
    #TODO: timestamp feature 
    # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # chat_line = f"[{timestamp}] {username}: {message}"
    chat_line = f"{username}: {message}"
    
    if room not in chat_rooms:
        chat_rooms[room] = [f"Room name: {room}"]

    chat_rooms[room].append(chat_line)
    
    return jsonify({"status": "Message saved"}), 201


############################### GET /api/chat/<room> ###############################
@chat.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    if room not in chat_rooms:
        return jsonify({"error": "Room not found"}), 404

    chat_log = "\n".join(chat_rooms[room])

    return chat_log, 200, {'Content-Type': 'text/plain; charset=utf-8'}


############################### GET <room> ###############################
@chat.route('/<room>', methods=['GET'])
def index_room(room):
    # Check if the room exists
    if room not in chat_rooms:
        return jsonify({"error": "Room not found"}), 404

    # Prepare chat log and room data to pass to the template
    chat_log = "\n".join(chat_rooms[room])

    # Pass room and chat_log to the template
    return render_template('index.html', room=room, chat_log=chat_log)


