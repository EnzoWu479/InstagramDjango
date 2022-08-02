from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from ..validate import emptyValue
def editarPerfil(req):
    if not req.user.is_authenticated:
        return redirect("login")
    if req.method == "POST":
        user = get_object_or_404(User, id=req.user.id)
        infos = {
            'username': req.POST['username'],
            'email': req.POST['email'],
            'description': req.POST['description']
        }
        if req.POST['profilePhoto']:
            infos['profilePhoto'] = req.POST['profilePhoto']
            user.profile.photo = infos['profilePhoto']
        
        print(infos)
        user.username = infos['username']
        user.email = infos['email']
        user.profile.description = infos['description']
        user.save()
        return redirect('index')
    return render(req, 'editarPerfil/editarPerfil.html')

def alterarSenha(req):
    if not req.user.is_authenticated:
        return redirect("login")
    if req.method == "POST":
        pass
    return render(req, 'editarPerfil/alterarSenha.html')