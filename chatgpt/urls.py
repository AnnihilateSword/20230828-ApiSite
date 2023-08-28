from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatgpt, name='chatgpt'),
    path('generate', views.generate, name='generate'),
    path('generate_stream', views.generate_stream, name='generate_stream'),
    path('generate_image', views.generate_image, name='generate_image'),
]