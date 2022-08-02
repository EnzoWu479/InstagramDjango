from django.contrib.auth.models import User
from django.contrib import auth, messages
from ..validate import emptyValue, equal
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Foto
from django.http import HttpResponseRedirect
def register(req):
    '''Registra um novo usuário'''
    if req.method == "POST":
        infos = {
            'email':        req.POST['email'],
            'username':     req.POST['username'],
            'password':     req.POST['password'],
            'password1':    req.POST['password1'],
            'photo':        req.FILES['profilePhoto'],
        }
        if emptyValue(infos['email']):
            messages.error(req, "Preencha o campo do email")
            return redirect("register")
        
        if emptyValue(infos['username']):
            messages.error(req, "Preencha o campo de username")
            return redirect("register")
        
        if emptyValue(infos['password']):
            messages.error(req, "Preencha o campo da senha")
            return redirect("register")

        if not equal(infos['password'], infos['password1']):
            messages.error(req, "As senhas não são iguais")
            print("As senhas não são iguais")
            return redirect("register")
        
        if User.objects.filter(email=infos['email']).exists():
            messages.error(req, "Email já registrado")
            print("Email já registrado")
            return redirect("register")
        
        if User.objects.filter(username=infos['username']).exists():
            messages.error(req, "Nome de usuário já registrado")
            print("Nome de usuário já registrado")
            return redirect("register")

        user = User.objects.create_user(
            username=infos['username'],
            email=infos['email'],
            password=infos['password'],
        )
        profile = user.profile
        profile.photo = infos['photo']
        profile.photo_100 = infos['photo']
        profile.photo_256 = infos['photo']
        profile.save()
        messages.success(req, "Usuário criado com sucesso")
        print("user Criado")
        return redirect("login")
    return render(req, 'user/register.html')

def login(req):
    '''Faz o login de um usuário'''
    if req.method == "POST":
        infos = {
            'email': req.POST['email'],
            'password': req.POST['password']
        }
        if emptyValue(infos['email']) or emptyValue(infos['password']):
            messages.error(req, "Preencha os campos de email e senha")
            return redirect("login")
        if User.objects.filter(email=infos["email"]).exists():
            username = User.objects.filter(email=infos["email"]).values_list("username", flat=True).get()
            user = auth.authenticate(req, username=username, password=infos["password"])
            if user is not None:
                auth.login(req, user)
                return redirect('index')
    return render(req, 'user/login.html')

def logout(req):
    '''Desloga um usuário'''
    auth.logout(req)
    return redirect("login")

def profile(req, user_id):
    if not req.user.is_authenticated:
        return redirect("login")
    user = get_object_or_404(User, pk=user_id)
    fotos = Foto.objects.order_by('-publishData').filter(profile=user)
    dados = {
        'profile': user,
        'fotos': fotos
    }
    return render(req, 'user/profile.html', dados)
def profilesaved(req):
    if not req.user.is_authenticated:
        return redirect("login")
    fotos = req.user.profile.saved.all
    dados = {
        "fotos": fotos
    }
    return render(req, 'user/profileSave.html', dados)

def ProfileFollow(req, user_id):
    if not req.user.is_authenticated:
        return redirect("login")
    user = get_object_or_404(User, pk=user_id)
    if user in req.user.profile.following.all():
        req.user.profile.following.remove(user)
    else:
        req.user.profile.following.add(user)
    return HttpResponseRedirect(req.POST['next'])
