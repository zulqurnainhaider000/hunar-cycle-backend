from flask_socketio import SocketIO

# Initialize socketio without the app initially to avoid circular imports
socketio = SocketIO(cors_allowed_origins="*")

# Import the socket event handlers so they register with the socketio instance
from . import dojo_sockets
from . import chat_sockets
