from django.shortcuts import render

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
