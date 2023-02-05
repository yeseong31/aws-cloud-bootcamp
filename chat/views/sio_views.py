import os

import socketio
from django.http import HttpResponse

from config.settings.base import BASE_DIR

# set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's installed
async_mode = 'eventlet'

sio = socketio.Server(
    async_mode=async_mode,
    cors_allowed_origins='*',
    logger=True,
    async_handlers=True,
    pingTimeout=900
)
thread = None

to_client = dict()


def chat(request):
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return HttpResponse(open(os.path.join(BASE_DIR, 'templates/chat.html')))


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {'data': '[Server] Server generated event'}, namespace='/test')


@sio.event
def on_connect(sid, environ):
    """
    SocketIO Connect 이벤트

    :param sid:
    - SocketIO ID

    :return(emit):
    - message: emit 설명
    - sid: SocketIO ID
    """
    sio.emit('connect', {'message': '[Server] Connected', 'sid': sid})


@sio.event
def on_disconnect(sid):
    """
    SocketIO Disconnect 이벤트

    :param sid:
    - SocketIO ID

    :return(emit):
    - message: emit 설명
    """
    sio.emit('disconnect', {'message': '[Server] Disconnected'})


@sio.on('message')
def on_message(sid, msg):
    """
    Socket Message 이벤트

    :param sid:
    - SocketIO ID

    :param msg:
    - 메시지 내용

    :return(emit):
    - msg: 메시지 내용
    """
    if msg == 'New Connect!':
        to_client['message'] = 'welcome!'
        to_client['type'] = 'connect'
        sio.emit('status', {'msg': 'connect'})
    elif msg == 'Disconnect':
        to_client['message'] = 'bye bye'
        to_client['type'] = 'disconnect'
        sio.emit('status', {'msg': 'disconnect'})
    else:
        to_client['message'] = msg
        to_client['type'] = 'normal'
        sio.emit('status', {'msg': f'message: {msg}'})
    sio.send(to_client, broadcast=True)
