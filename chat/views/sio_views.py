import socketio

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


@sio.on('join')
def on_join(sid, data):
    """
    SocketIO 방 입장 이벤트
    
    :param sid:
    - SocketIO ID
    
    :param data:
    - nickname: 방 참가자 닉네임
    - roomCode: 방 코드
    
    :return(emit):
    - message: emit 설명
    - isSuccess: 방 입장 완료 여부
    """
    nickname = data['nickname']
    room_code = data['roomCode']
    
    sio.enter_room(sid, room_code)
    
    response_data = {
        'message': f"[Server] {nickname} has entered the room.",
        'isSuccess': True
    }

    sio.emit('join', response_data, room=room_code)


@sio.on('message')
def on_message(sid, data):
    """
    Socket Message 이벤트

    :param sid:
    - SocketIO ID

    :param data:
    - message: 메시지 내용
    - roomCode: 방 코드 (Connect 이벤트 발생 시에만 None)
    
    :return(send):
    - message: 메시지 내용
    - type: 메시지 타입
    - nickname: 메시지 대상(참가자) 닉네임
    """
    message = data['message']
    room_code = data.get('roomCode')
    nickname = data.get('nickname', '익명')

    to_client['nickname'] = nickname

    if message == 'CONNECT':
        to_client['message'] = f'{nickname} 님이 입장하였습니다.'
        to_client['type'] = 'connect'
    elif message == 'DISCONNECT':
        to_client['message'] = f'{nickname} 님이 퇴장하였습니다.'
        to_client['type'] = 'disconnect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'

    sio.send(to_client, room=room_code)
