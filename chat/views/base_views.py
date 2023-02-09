import secrets

from django.shortcuts import render, redirect

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
    :return:
    - code: 방 코드
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


def chat(request, room_code):
    """
    방 입장
    :param request:
    :return:
    """
    nickname = request.GET.get('nickname', request.session['nickname'])
    context = {
        'nickname': nickname,
        'roomCode': room_code
    }
    return render(request, 'chat.html', context)
