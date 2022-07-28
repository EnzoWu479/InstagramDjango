from django.shortcuts import redirect, render, get_object_or_404
from ..models import Foto
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(req):
    '''Feed principal'''
    if not req.user.is_authenticated:
        return redirect("login")
    photos = Foto.objects.order_by('-publishData').filter(private=False)
    dados = {
        'fotos': photos
    }
    return render(req, 'photo/index.html', dados)

def photo(req, foto_id):
    '''Página de vizualização de foto individual'''
    if not req.user.is_authenticated:
        return redirect("login")
    foto = get_object_or_404(Foto, pk=foto_id)
    dados = {
        'foto': foto
    }
    return render(req, 'photo/photo.html', dados)

def save(req, foto_id):
    """Salva um post em um perfil"""
    if not req.user.is_authenticated:
        return redirect("login")
    foto = get_object_or_404(Foto, pk=foto_id)
    if foto in req.user.profile.saved.all():
        req.user.profile.saved.remove(foto)
    else:
        req.user.profile.saved.add(foto)
    return HttpResponseRedirect(reverse('index'))
