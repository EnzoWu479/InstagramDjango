from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from ..models import Message
from ..validate import emptyValue
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

def chat(req):
    if not req.user.is_authenticated:
        return redirect("login")
    myaccount = get_object_or_404(User, pk=req.user.id)
    profiles = User.objects.filter(Q(followers__in=[req.user.id]) | Q(sended__receiver=myaccount) | Q(received__sender=myaccount)).distinct()
    dados = {
        'contas': profiles
    }
    return render(req, 'user/chat.html', dados)

def chatSomeone(req, user_id):
    if not req.user.is_authenticated:
        return redirect("login")
    myaccount = get_object_or_404(User, pk=req.user.id)
    hisaccount = get_object_or_404(User, pk=user_id)
    if req.method == "POST":
        msg = req.POST['message']
        if emptyValue(msg):
            return redirect('chatSomeone', user_id)
        message = Message.objects.create(
            sender=myaccount,
            receiver=hisaccount,
            message=msg,
        )
        message.save()
        return HttpResponse('Mensagem enviada')
    profiles = User.objects.filter(Q(followers__in=[req.user.id]) | Q(sended__receiver=myaccount) | Q(received__sender=myaccount)).distinct()
    conta = get_object_or_404(User, pk=user_id)
    dados = {
        'contas': profiles,
        'conta': conta,
    }
    return render(req, 'user/chatSomeone.html', dados)

def getMessage(req, user_id):
    if not req.user.is_authenticated:
        return redirect("login")
    myaccount = get_object_or_404(User, pk=req.user.id)
    hisaccount = get_object_or_404(User, pk=user_id)

    messages = Message.objects.order_by('dataTime').filter((Q(sender=myaccount) & Q(receiver=hisaccount)) | (Q(sender=hisaccount) & Q(receiver=myaccount)))
    return JsonResponse({'messages': list(messages.values())})