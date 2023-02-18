import secrets

from django.shortcuts import render, get_object_or_404, redirect

from chat.models import Room


def home(request):
    """
    전체 방 목록 조회
    
    :return:
    - room_list: 방 목록
    """
    room_list = Room.objects.order_by('-created_at')
    context = {'room_list': room_list}
    return render(request, 'home.html', context)


def enter_room(request):
    """
    방 생성 및 입장
    
    :param request:
    - type: 방 생성일 경우 'create', 입장일 경우 'enter', 그렇지 않으면 ''
    - participant(enter): 참가자 닉네임
    - roomCode(enter): 방 코드
    - owner(create): 방 생성자 닉네임
    - roomName(create): 방 이름
    """
    _type = request.POST.get('type')
    if _type == 'enter':
        nickname = request.POST.get('participant')
        room_code = request.POST.get('roomCode')
    
        room = get_object_or_404(Room, code=room_code)
    
        context = {
            'nickname': nickname,
            'room_name': room.name,
            'room_code': room.code
        }
        return render(request, 'chat.html', context)
    elif _type == 'create':
        owner = request.POST.get('owner')
        room_name = request.POST.get('roomName')
    
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
        return render(request, 'chat.html', context)
    else:
        return redirect('/home')
