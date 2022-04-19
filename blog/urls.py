from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('get_url', views.get, name='get'),
    path('post_url', views.post, name='post'),
]
