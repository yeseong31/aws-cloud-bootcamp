import secrets

from django.shortcuts import render, get_object_or_404, redirect

from chat.models import Room


def home(request):
    """
    전체 방 목록 조회
    
    :param request:
    - type: 방 생성일 경우 'CREATE', 입장일 경우 'ENTER', 그렇지 않으면 None
    :return:
    - room_list: 방 목록
    """
    _type = request.POST.get('type')
    
    if _type == 'ENTER':
        context = enter_room(request)
        return render(request, 'chat.html', context)
    elif _type == 'CREATE':
        context = create_room(request)
        return render(request, 'chat.html', context)
    else:
        room_list = Room.objects.order_by('-created_at')
        context = {'room_list': room_list}
        return render(request, 'index.html', context)


def enter_room(request):
    """
    방 입장
    
    :param request:
    - participant: 참가자 닉네임
    - roomId: 방 번호
    :return:
    - nickname: 참가자 닉네임
    - room_name: 방 이름
    - room_code: 방 코드
    """
    nickname = request.POST.get('participant')
    room_id = request.POST.get('roomId')

    room = get_object_or_404(Room, id=room_id)

    context = {
        'nickname': nickname,
        'room_name': room.name,
        'room_code': room.code
    }

    return context


def create_room(request):
    """
    방 생성
    
    :param request:
    - ownerName: 방 생성자 닉네임
    - sendRoomName: 방 이름
    :return:
    - nickname: 참가자 닉네임
    - room_name: 방 이름
    - room_code: 방 코드
    """
    owner = request.POST.get('ownerName')
    room_name = request.POST.get('sendRoomName')

    # 새로운 방 생성
    room = Room(
        name=room_name,
        code=secrets.token_urlsafe(5),
        owner=owner
    )
    room.save()

    context = {
        'nickname': f'⭐{owner}',
        'room_name': room.name,
        'room_code': room.code
    }
    
    return context
