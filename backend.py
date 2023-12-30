from flask import Flask, render_template, request
from flask_socketio import SocketIO
import random
import string

app = Flask(__name__)
socketio = SocketIO(app)
custom_id_to_sid = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    socketio.emit('message', 'Client ' + str(session_id) + ": " + msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
def generate_custom_id():
    # Generate a random 6-character alphanumeric custom ID
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))