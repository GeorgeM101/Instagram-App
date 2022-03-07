from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    bio  = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)
    description = models.CharField(max_length=800, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_on']
    
    def __str__(self):
        return self.description

    def save_post(self):
        self.save()

    def delete_image(self):
        self.delete()