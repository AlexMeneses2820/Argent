from django.db import models
from django.conf import settings

class BaseModel(models.Model):

    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
