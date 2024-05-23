from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import MotionMainPost

# Create your views here.

'''def home (request):
    return render (request, 'home.html',{})'''

def base (request):
    return render(request,"base.html")

#The main HomeView page
class HomeView(ListView):
    model = MotionMainPost
    template_name = 'motion/home.html'

#About page of the blog
def AboutView (request):
    return render(request, 'motion/about_us.html', {})