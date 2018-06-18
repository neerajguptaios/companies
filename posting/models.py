from django.conf import settings
from django.db import models

class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=true, blank=true)
    content = models.TextField(max_length=120, null=true, blank=true)
    timestamp = models.DateTimeField(auto_now_add=true)

    def __str__(self):
        return self.user