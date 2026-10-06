from flask_socketio import emit, join_room, leave_room
from . import socketio

@socketio.on('join_turf')
def handle_join_turf(data):
    room = data.get('turf_id')
    user_name = data.get('username')
    if room:
        join_room(room)
        emit('chat_msg', {'sender': 'System', 'text': f'{user_name} joined the turf.', 'timestamp': 'Just now'}, to=room)

@socketio.on('send_message')
def handle_send_message(data):
    room = data.get('turf_id')
    message = data.get('text')
    user_name = data.get('username')
    
    if room and message:
        # Broadcast to everyone in the room, including sender to confirm it was sent
        emit('chat_msg', {
            'sender': user_name,
            'text': message,
            'timestamp': 'Just now'
        }, to=room)
