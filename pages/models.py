from django.db import models

# Create your models here.
class contact(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=12)
    country=models.CharField(max_length=50)
    query=models.TextField()
    date_time=models.DateTimeField()
    
    def __str__(self):
        return self.username

class blogs(models.Model):
    username=models.CharField(max_length=30)
    title=models.CharField(max_length=20)
    blog=models.TextField()
    date_time=models.DateTimeField()
    def __str__(self):
        user_name=self.username
        blog_title=self.title
        title=user_name+" "+blog_title
        return title
    