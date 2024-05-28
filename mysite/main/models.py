from django.db import models
from django.contrib.auth.models import User

class Memories(models.Model):
    name_memorie = models.CharField('Name', max_length=150)
    date_memorie = models.DateField('Date of memorie')
    description_memorie = models.TextField()
    place = models.CharField(max_length=150, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name_memorie
    


