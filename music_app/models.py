from django.db import models
from django.contrib.auth.models import User



class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    ACCESS_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music_files')
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default=PUBLIC)
    allowed_emails = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.file.name
# Create your models here.
