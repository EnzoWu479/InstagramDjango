from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('discover', discover, name="discover"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('publish', publish, name='publish'),
    path('photo/<int:foto_id>', photo, name="photo"),
    path('logout', logout, name="logout"),
    path('edit/<int:foto_id>', edit, name='edit'),
    path('deletePhoto/<int:foto_id>', deletePhoto, name="deletePhoto"),
    path('updatePhoto/<int:foto_id>', updatePhoto, name='updatePhoto'),
    path('profile/editar', editarPerfil, name="editarPerfil"),
    path('profile/alterarSenha', alterarSenha, name="alterarSenha"),
    path('profile/<int:user_id>', profile, name="profile"),
    path('profilesaved', profilesaved, name="profilesaved"),
    path('like', like, name="likePost"),
    path('save/<int:foto_id>', save, name="savePost"),
    path('comment/<int:foto_id>', comment, name="commentPost"),
    path('follow/<int:user_id>', ProfileFollow, name="follow"),
    path('direct/inbox/<int:user_id>', chatSomeone, name="chatSomeone"),
    path('direct/inbox', chat, name="chat"),
    path('direct/getMessage/<int:user_id>', getMessage, name="getMessage")
]