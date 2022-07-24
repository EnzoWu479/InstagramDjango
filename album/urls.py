from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('publish', views.publish, name='publish'),
    path('photo', views.photo, name="photo"),
]