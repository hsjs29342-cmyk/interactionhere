from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + " has joined the room.", to=room)

@socketio.on('message')
def handle_message(data):
    send(data, to=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
