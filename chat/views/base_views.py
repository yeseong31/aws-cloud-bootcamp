import secrets

from django.shortcuts import render, redirect, get_object_or_404

from chat.models import Room


def home(request):
    """
    전체 방 목록 조회
    
    :return:
    - room_list: 방 목록
    """
    room_list = Room.objects.all().order_by('-created_at')
    context = {'room_list': room_list}
    return render(request, 'home.html', context)


def create_room(request):
    """
    새로운 방 생성
    
    :param request:
    - owner: 방 생성자 닉네임
    - roomName: 방 이름
    """
    owner = request.POST.get('owner')
    room_name = request.POST.get('roomName')
    
    # 새로운 방 생성
    room = Room(
        name=room_name,
        code=secrets.token_urlsafe(5),
        owner=owner
    )
    room.save()
    
    request.session['nickname'] = owner
    return redirect(f'/chat/{room.code}/')


def enter_room(request, room_code):
    """
    방 입장
    
    :param room_code:
    - 입장하고자 하는 방 코드
    """
    nickname = request.GET.get('nickname', request.session['nickname'])
    room = get_object_or_404(Room, code=room_code)

    context = {
        'nickname': nickname,
        'room_name': room.name,
        'roomCode': room_code
    }
    return render(request, 'chat.html', context)
