from django.shortcuts import redirect, render
from django.contrib import auth, messages
from .models import Foto
from .validate import emptyValue, equal
from django.contrib.auth.models import User

def index(req):
    if not req.user.is_authenticated:
        return render("login")
    photos = Foto.objects.order_by('description')
    dados = {
        'fotos': photos
    }
    return render(req, 'index.html', dados)

def login(req):
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
    return render(req, 'login.html')

def register(req):
    if req.method == "POST":
        infos = {
            'email': req.POST['email'],
            'username': req.POST['username'],
            'password': req.POST['password'],
            'password1': req.POST['password1'],
            'photo': req.FILES['profilePhoto'],
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
        profile.save()
        messages.success(req, "Usuário criado com sucesso")
        print("user Criado")
        return redirect("login")
    return render(req, 'register.html')

def publish(req):
    if not req.user.is_authenticated:
        return redirect("login")
    if req.method == "POST":
        infos = {
            'photo': req.FILES['photoPublic'],
            'description': req.POST['description']
        }
        
    return render(req, 'publish.html')

def photo(req):
    if not req.user.is_authenticated:
        return redirect("login")
    return render(req, 'photo.html')

def logout(req):
    auth.logout(req)
    return redirect("login")