from django.shortcuts import redirect, render, get_object_or_404
from ..models import Foto
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from random import sample

def index(req):
    '''Feed principal'''
    if not req.user.is_authenticated:
        return redirect("login")
    photos = Foto.objects.order_by('-publishData').filter(Q(profile__followers__in=[req.user.id]) | Q(profile=req.user))
    sugestions = list(User.objects.exclude(pk=req.user.id))
    nsugest = 0
    if len(sugestions) >= 3:
        nsugest = 3
    else:
        nsugest = len(sugestions)
    sugestions = sample(sugestions, nsugest)
    dados = {
        'fotos': photos,
        'sugestions': sugestions
    }
    return render(req, 'photo/index.html', dados)

def discover(req):
    '''Feed principal'''
    if not req.user.is_authenticated:
        return redirect("login")
    photos = Foto.objects.order_by('-publishData')
    followed = User.objects.exclude(pk=req.user.id).filter(followers__in=[req.user.id])
    suggestUsers = User.objects.exclude(pk=req.user.id).exclude(followers__in=[req.user.id])
    dados = {
        'fotos': photos,
        'suggestUsers': suggestUsers,
        'followed': followed,

    }
    return render(req, 'photo/discover.html', dados)
    
def photo(req, foto_id):
    '''Página de vizualização de foto individual'''
    if not req.user.is_authenticated:
        return redirect("login")
    foto = get_object_or_404(Foto, pk=foto_id)
    dados = {
        'foto': foto
    }
    return render(req, 'photo/photo.html', dados)


