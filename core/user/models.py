from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from app.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):

    image = models.ImageField(upload_to='users/%y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/UsuarioBase.jpg')



