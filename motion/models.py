from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
    
# The main model for Deus Magnus Model category
class MotionMainPost(models.Model):
    mobile_title = models.CharField(max_length=255, blank=True, null=True)
    mobile_description = models.TextField()
    mobile_slug = models.SlugField (max_length=255,blank=True, null=True)
    deus_manus_video = models.FileField(upload_to='videos/')
    #thumbnail = models.ImageField(max_length=100, null=True, blank=True)
    mobile_publish_date = models.DateTimeField (auto_now_add= True)
    mobile_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-mobile_publish_date']
    
    def __str__(self):
        return self.mobile_title + ' | ' + str(self.mobile_author)
    
    def get_absolute_url(self):
        return reverse('home',)