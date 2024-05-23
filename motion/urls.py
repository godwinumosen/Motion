from django.urls import path
from . import views
from .views import HomeView #ArticleDetailView,

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
]