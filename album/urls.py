from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('publish', publish, name='publish'),
    path('photo/<int:foto_id>', photo, name="photo"),
    path('logout', logout, name="logout"),
    path('edit/<int:foto_id>', edit, name='edit'),
    path('deletePhoto/<int:foto_id>', deletePhoto, name="deletePhoto"),
    path('updatePhoto/<int:foto_id>', updatePhoto, name='updatePhoto'),
    path('profile/<int:user_id>', profile, name="profile"),
    path('profilesaved', profilesaved, name="profilesaved"),
    path('like/<int:foto_id>', like, name="likePost"),
    path('save/<int:foto_id>', save, name="savePost")
]