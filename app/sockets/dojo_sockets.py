from flask_socketio import emit, join_room, leave_room
from . import socketio
import uuid
from flask import request

# Memory structure: { 'TECH': [ {sid, user_id, username, level} ] }
matchmaking_queue = {}

@socketio.on('find_match')
def handle_find_match(data):
    category = data.get('category')
    user_id = data.get('user_id')
    username = data.get('username')
    level = data.get('level')
    sid = request.sid

    if not category or not user_id:
        return

    if category not in matchmaking_queue:
        matchmaking_queue[category] = []
    
    queue = matchmaking_queue[category]
    
    # Remove self to prevent matching with self
    queue = [p for p in queue if p['user_id'] != user_id]

    if len(queue) > 0:
        # Match found! Pop the longest waiting opponent
        opponent = queue.pop(0)
        matchmaking_queue[category] = queue 
        
        session_id = f"duel-{uuid.uuid4()}"
        
        # Notify Opponent
        emit('match_found', {
            'session_id': session_id,
            'opponent': {'username': username, 'level': level, 'user_id': user_id}
        }, to=opponent['sid'])
        
        # Notify Current User
        emit('match_found', {
            'session_id': session_id,
            'opponent': {'username': opponent['username'], 'level': opponent['level'], 'user_id': opponent['user_id']}
        }, to=sid)
        
    else:
        # Add to queue
        queue.append({
            'sid': sid,
            'user_id': user_id,
            'username': username,
            'level': level
        })
        matchmaking_queue[category] = queue

@socketio.on('cancel_search')
def handle_cancel_search(data):
    category = data.get('category')
    user_id = data.get('user_id')
    if category in matchmaking_queue:
        matchmaking_queue[category] = [p for p in matchmaking_queue[category] if p['user_id'] != user_id]

@socketio.on('join_dojo')
def handle_join_dojo(data):
    room = data.get('session_id')
    user_id = data.get('user_id')
    if room:
        join_room(room)
        emit('dojo_system_msg', {'msg': f'User {user_id} has joined the duel.'}, to=room)

@socketio.on('submit_score')
def handle_submit_score(data):
    room = data.get('session_id')
    score = data.get('score')
    user_id = data.get('user_id')
    if room:
        # Broadcast the score update to the opponent (exclude self)
        emit('score_update', {'user_id': user_id, 'score': score}, to=room, include_self=False)
