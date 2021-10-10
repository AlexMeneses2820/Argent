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




#class BaseModel(models.Model):
 #   user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
  #  date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   # user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated')
    #date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    #class Meta:
     #   abstract = True
