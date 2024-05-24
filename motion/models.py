from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
    
# The main model for Deus Magnus Model category
class MotionMainPost(models.Model):
    motion_title = models.CharField(max_length=255, blank=True, null=True)
    motion_description = models.TextField()
    motion_slug = models.SlugField (max_length=255,blank=True, null=True)
    #motion_video = models.FileField(upload_to='videos/')
    motion_img = models.ImageField(upload_to='images/')
    motion_publish_date = models.DateTimeField (auto_now_add= True)
    motion_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-motion_publish_date']
    
    def __str__(self):
        return self.motion_title + ' | ' + str(self.motion_author)
    
    def get_absolute_url(self):
        return reverse('home',)
    
#The blog category
class BlogMotion(models.Model):
    blog_motion_title = models.CharField(max_length=255, blank=True, null=True)
    blog_motion_description = models.TextField()
    blog_motion_slug = models.SlugField (max_length=255,blank=True, null=True)
    blog_motion_img = models.ImageField(upload_to='blog_images/')
    blog_motion_publish_date = models.DateTimeField (auto_now_add= True)
    blog_motion_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-blog_motion_publish_date']
    
    def __str__(self):
        return self.blog_motion_title + ' | ' + str(self.blog_motion_author)
    
    def get_absolute_url(self):
        return reverse('home',)