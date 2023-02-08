from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=128, verbose_name='방 이름')
    code = models.CharField(max_length=7, unique=True, verbose_name='방 코드')
    description = models.TextField(verbose_name='방 설명', null=True, blank=True)
    owner = models.CharField(max_length=128, verbose_name='방장 이름')
    current = models.IntegerField(default=0, verbose_name='현재 참여 인원 수')
    total = models.IntegerField(default=30, verbose_name='최대 참여 인원 수')
    created_at = models.DateTimeField(verbose_name='생성일', default=timezone.now)
    modified_at = models.DateTimeField(verbose_name='수정일', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
