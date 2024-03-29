from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from ..models import Foto, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def publish(req):
    '''Pagina de publicação da foto'''
    if not req.user.is_authenticated:
        return redirect("login")
    if req.method == "POST":
        infos = {
            'photo':        req.FILES['photoPublic'],
            'description':  req.POST['description'],
            'profile':      get_object_or_404(User, pk=req.user.id),
        }
        #if 'private' in req.POST:
        #    infos['private'] = req.POST['private']
        #else:
        infos['private'] = False
        if not infos['private']:
        #    infos['publishData'] = date.today()
            photo = Foto.objects.create(
                photo       = infos['photo'],
                photo_512 = infos['photo'],
                description = infos['description'],
                profile     = infos['profile'],
                private     = infos['private'],
        #        publishData = infos['publishData']
            )
        else:
            photo = Foto.objects.create(
                photo       = infos['photo'],
                photo_512   = infos['photo'],
                description = infos['description'],
                profile     = infos['profile'],
                private     = infos['private'],
            )
        photo.save()
        return redirect('index')
    return render(req, 'photo/publish.html')

def edit(req, foto_id):
    '''Página de edição da publicação'''
    if not req.user.is_authenticated:
        return redirect("login")
    photo = get_object_or_404(Foto, pk=foto_id)
    if photo.profile != req.user:
        return redirect('index')
    photoEdit = {
        'photo': photo
    }
    return render(req, 'photo/edit.html', photoEdit)

def updatePhoto(req, foto_id):
    '''Atualiza as informações da foto'''
    if not req.user.is_authenticated:
        return redirect("login")
    if req.method == 'POST':
        photo = get_object_or_404(Foto, pk=foto_id)
        photo.description = req.POST['description']
        photo.save()
        return redirect('index')

def deletePhoto(req, foto_id):
    '''Deleta a foto'''
    if not req.user.is_authenticated:
        return redirect("login")
    photo = get_object_or_404(Foto, pk=foto_id)
    photo.delete()
    return redirect('index')

def save(req, foto_id):
    """Salva um post em um perfil"""
    if not req.user.is_authenticated:
        return redirect("login")
    foto = get_object_or_404(Foto, pk=foto_id)
    if foto in req.user.profile.saved.all():
        req.user.profile.saved.remove(foto)
    else:
        req.user.profile.saved.add(foto)
    return HttpResponse('Save enviado')

def like(req, item_id):
    if not req.user.is_authenticated:
        return redirect("login")
    post = get_object_or_404(Foto, id=item_id)
    if req.user in post.likes.all():
        post.likes.remove(req.user)
    else:
        post.likes.add(req.user)
    return HttpResponse('Like enviado')

def comment(req, foto_id):
    if not req.user.is_authenticated:
        return redirect("login")
    post = get_object_or_404(Foto, id=foto_id)
    comment = Comment.objects.create(
        foto = post,
        profile = get_object_or_404(User, pk=req.user.id),
        body = req.POST['commentary'],
    )
    comment.save()
    return HttpResponse('Comentário enviado')