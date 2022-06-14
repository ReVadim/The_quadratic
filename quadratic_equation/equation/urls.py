from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('comment/new/', views.comment_page, name='comment_page')
]
