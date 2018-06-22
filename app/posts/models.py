from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)



