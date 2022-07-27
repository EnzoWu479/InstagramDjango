from django.shortcuts import redirect, render
from ..models import Foto


def index(req):
    '''Feed principal'''
    if not req.user.is_authenticated:
        return redirect("login")
    photos = Foto.objects.order_by('-publishData').filter(private=False)
    dados = {
        'fotos': photos
    }
    return render(req, 'photo/index.html', dados)

def photo(req):
    '''Página de vizualização de foto individual'''
    if not req.user.is_authenticated:
        return redirect("login")
    return render(req, 'photo/photo.html')

