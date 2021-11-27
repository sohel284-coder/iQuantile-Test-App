from os import name
from django.db import models
from django.contrib.auth.models import User
import datetime


class FileManagement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=32, )
    files = models.ImageField(upload_to='files', null=True, blank=True, )
    descriptions = models.TextField()
    date = models.DateTimeField(auto_now_add=True, )

    @property
    def delete_after_thirty_minutes(self):
        if self.date < datetime.datetime.now()-datetime.timedelta(minutes=30):
            e = FileManagement.objects.get(pk=self.pk)
            e.delete()
            return True
        else:
            return False

    def __str__(self):
        return self.name
