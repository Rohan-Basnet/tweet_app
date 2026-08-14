from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=200)
    image=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)#creates the timestamp once when the object is created
    updated_at=models.DateTimeField(auto_now=True)# updates the timestamp everytime object is saved
    # comments=models.TextField(max_length=200,blank=True,null=True)
    def __str__(self):
        return f'{self.user.username} - {self.text[:50]}'

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=200, blank=True)
    profile_picture=models.ImageField(upload_to='profile_pics/',blank=True,null=True)

    def __str__(self):
        return f'{self.user.username}-{self.bio[:50]}'

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    tweet=models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    text= models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:50]}'


class Like(models.Model):
    user= models.ForeignKey(User , on_delete= models.CASCADE, related_name='likes')
    tweet= models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
    liked_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.tweet.text[:50]}'
# Create your models here.
