from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView,BlogView,BlogArticleDetail

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('message/', views.message, name='message'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog_article/<int:pk>/', BlogArticleDetail.as_view(), name="blog_detail"),
]