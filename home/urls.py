from django.urls import path
from .views import *

app_name = 'index'
urlpatterns = [
    path('' , home_views , name = 'index'),
    path('about' , about_views , name='about'),
    path('take_action' , take_action_views , name='take_action'),
    path('news' , news_views , name='news'),
    path('doctores' , doctores_views , name='doctores'),
    path('contact' , contact_views , name='contact')
]


