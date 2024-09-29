from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initial toggle state
toggle_state = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle')
def handle_toggle():
    global toggle_state
    # Toggle the state
    toggle_state = not toggle_state
    state_message = 'ON' if toggle_state else 'OFF'
    
    # Broadcast the new state to all connected clients
    emit('toggle_update', state_message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
