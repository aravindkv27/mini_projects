from chatapp import create_app
from flask_socketio import join_room, leave_room, send, SocketIO


app = create_app()


if __name__ == '__main__':

    app.run(debug=True)