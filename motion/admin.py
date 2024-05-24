from django.contrib import admin
# Register your models here.
from . import models
from .models import MotionMainPost,BlogMotion
#The DeusMagnus post post model admin of josepdam
class MotionMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'motion_slug': ('motion_title',)}
    list_display = ['motion_title','motion_description','motion_img','motion_author']
admin.site.register(MotionMainPost, MotionMainPostModelAdmin)

#This blog is for Deus Magnus blog Page & News
class BlogMotionModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'blog_motion_slug': ('blog_motion_title',)}
    list_display = ['blog_motion_title','blog_motion_description','blog_motion_img','blog_motion_author']
admin.site.register(BlogMotion, BlogMotionModelAdmin)

