from django.contrib import admin
# Register your models here.
from . import models
from .models import MotionMainPost
#The DeusMagnus post post model admin of josepdam
class MotionMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'motion_slug': ('motion_title',)}
    list_display = ['motion_title','motion_description','motion_img','motion_author']
admin.site.register(MotionMainPost, MotionMainPostModelAdmin)
