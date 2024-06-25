from django.db import models
from django.contrib.auth. models import User


class UserProfile(models.Model):
  
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile',null=True)
    username = models.CharField(max_length=30,null=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    profile_image = models.ImageField(upload_to='user-images',verbose_name='User Profile Image',null=True)

    def __str__(self):
        return str(self.user)