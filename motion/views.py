from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

'''def home (request):
    return render (request, 'home.html',{})'''

def base (request):
    return render(request,"base.html")

#The main HomeView page
class HomeView(ListView):
    model = DeusMagnusMainPost
    template_name = 'deus_magnus/home.html'