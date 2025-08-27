from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name