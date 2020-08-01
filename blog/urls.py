from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='education'), 
    path('post', views.post, name='social'),  
    path('post', views.post, name='politic'),  
    path('post', views.post, name='business'), 
    path('post', views.post, name='health'),    
]