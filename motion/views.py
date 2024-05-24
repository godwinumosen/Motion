from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import MotionMainPost
from django.contrib import messages

# Create your views here.

'''def home (request):
    return render (request, 'home.html',{})'''

def base (request):
    return render(request,"base.html")

#The main HomeView page
class HomeView(ListView):
    model = MotionMainPost
    template_name = 'motion/home.html'

 #The first motion ArticleDetailView page
class ArticleDetailView(DetailView):
    model = MotionMainPost
    template_name = 'motion/article_detail.html'
    def ArticleDetailView(request, pk):  
        object = get_object_or_404(MotionMainPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})

#About page of the blog
def AboutView (request):
    return render(request, 'motion/about_us.html', {})


# The Contact view been implemented
def ContactView (request):
    email='motion@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message'] 
        messages.success(request, f'Your email was Successfully sent to iMotion ({message_name})..!')
        return redirect('/message')
    else:
        context={
            'email':email
        }
        return render(request, 'motion/contact_us.html',context)

def message (request):
    return render (request, 'motion/message.html', {})