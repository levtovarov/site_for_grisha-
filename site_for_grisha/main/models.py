from django.db import models
from site_for_grisha.settings import MEDIA_ROOT


class Rock(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title


class RockDemo(models.Model):
    title = models.CharField('Название', max_length=50)
    rockers = models.TextField('Рокеры')
    popular_songs = models.TextField('Топ 5 песен')
    time_life = models.CharField('Время существования', max_length=15)
    biography = models.TextField('Биография')
    songs_mp3 = models.TextField('Песни')
    photos = models.TextField('Фото')

    def __str__(self):
        return self.title

# Create your models here.


class Cover(models.Model):
    title = models.CharField('Название', max_length=50, null=True, error_messages={'required': '', 'blank': '', 'null': ''}, blank=False)
    creator = models.CharField('Исполнитель', max_length=50, null=True, error_messages={'required': '', 'blank': '', 'null': ''}, blank=True)
    file = models.FileField('Кавер', upload_to=MEDIA_ROOT, null=True, error_messages={'required': '', 'blank': '', 'null': ''}, blank=True)

    def __str__(self):
        return self.title


